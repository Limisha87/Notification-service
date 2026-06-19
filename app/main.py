from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import engine, Base, SessionLocal
from .models import User, Notification
from .auth import get_current_user

from .schemas import (
    UserCreate,
    UserLogin,
    NotificationCreate,
    NotificationStatusUpdate
)
from .auth import (
    hash_password,
    verify_password,
    create_access_token
)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Omix Notification Service")


# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Home Route
@app.get("/")
def home():
    return {"message": "API Running"}


# Register API
@app.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    hashed_password = hash_password(user.password)

    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully"
    }


# Login API
@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        user.password,
        db_user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {"sub": db_user.email}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# Create Notification
@app.post("/notifications")
def create_notification(
    notification: NotificationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    new_notification = Notification(
        title=notification.title,
        message=notification.message,
        channel=notification.channel,
        status=notification.status,
        user_id=current_user.id
    )

    db.add(new_notification)
    db.commit()
    db.refresh(new_notification)

    return {
        "message": "Notification created successfully",
        "id": new_notification.id
    }


# Get All Notifications
@app.get("/notifications/{notification_id}")
def get_notification(
    notification_id: int,
    db: Session = Depends(get_db)
):

    notification = db.query(Notification).filter(
        Notification.id == notification_id
    ).first()

    if not notification:
        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )

    return notification

@app.put("/notifications/{notification_id}")
def update_notification_status(
    notification_id: int,
    update: NotificationStatusUpdate,
    db: Session = Depends(get_db)
):

    notification = db.query(Notification).filter(
        Notification.id == notification_id
    ).first()

    if not notification:
        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )

    notification.status = update.status

    db.commit()

    return {
        "message": "Status updated successfully"
    }
    
    
@app.delete("/notifications/{notification_id}")
def delete_notification(
    notification_id: int,
    db: Session = Depends(get_db)
):

    notification = db.query(Notification).filter(
        Notification.id == notification_id
    ).first()

    if not notification:
        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )

    db.delete(notification)
    db.commit()

    return {
        "message": "Notification deleted successfully"
    }
    
@app.get("/notifications/search/{title}")
def search_notification(
    title: str,
    db: Session = Depends(get_db)
):

    notifications = db.query(Notification).filter(
        Notification.title.contains(title)
    ).all()

    return notifications

@app.get("/notifications/status/{status}")
def filter_status(
    status: str,
    db: Session = Depends(get_db)
):

    notifications = db.query(Notification).filter(
        Notification.status == status
    ).all()

    return notifications