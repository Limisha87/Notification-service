# Notification Service API

A Mini Notification Service built using FastAPI, PostgreSQL, JWT Authentication, Docker, and Postman.

## Features

* User Registration
* User Login
* JWT Authentication
* Create Notifications
* Get Notifications
* Search Notifications
* Filter Notifications
* PostgreSQL Database
* Docker Support
* Render Deployment Ready

---

## Tech Stack

* Python 3.11
* FastAPI
* PostgreSQL
* JWT Authentication
* Docker
* Postman

---

## Project Structure

```text
notification-service/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   └── routes/
│
├── Dockerfile
├── .dockerignore
├── requirements.txt
├── render.yaml
├── .env
└── README.md
```

---

## Environment Variables

Create a `.env` file:

```env
DATABASE_URL=postgresql://username:password@host/database_name
SECRET_KEY=omix_secret_key_123
```

---

## Installation

### Clone Repository

```bash
git clone <repository_url>
cd notification-service
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
uvicorn app.main:app --reload
```

Application URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Register User

```http
POST /register
```

Request Body:

```json
{
  "username": "limisha",
  "email": "limisha@gmail.com",
  "password": "123456"
}
```

---

### Login User

```http
POST /login
```

Request Type:

```text
x-www-form-urlencoded
```

Parameters:

```text
username=limisha
password=123456
```

Response:

```json
{
  "access_token": "jwt_token",
  "token_type": "bearer"
}
```

---

### Create Notification

```http
POST /notifications
```

Header:

```http
Authorization: Bearer <access_token>
```

---

### Get Notifications

```http
GET /notifications
```

Header:

```http
Authorization: Bearer <access_token>
```

---

### Search Notifications

```http
GET /notifications?search=keyword
```

---

### Filter Notifications

```http
GET /notifications?status=read
```

---

## Docker

### Build Docker Image

```bash
docker build -t notification-service .
```

### Run Docker Container

```bash
docker run --env-file .env -p 8000:8000 notification-service
```

### Run Detached Mode

```bash
docker run -d --env-file .env -p 8000:8000 --name notification-api notification-service
```

### Check Running Containers

```bash
docker ps
```

### View Logs

```bash
docker logs notification-api
```

---

## Deployment

Application can be deployed on Render using:

* Dockerfile
* PostgreSQL Database
* Environment Variables

---

## Postman Collection
```

Test all APIs directly from Postman.

---

## Author

Limisha Gorakhpuriya


