# Omix Notification Service

## Overview

A FastAPI-based Notification Service with JWT Authentication and MySQL Database.

## Features

* User Registration
* User Login
* JWT Authentication
* Create Notification
* View All Notifications
* View Notification By ID
* Update Notification Status
* Delete Notification
* Search Notifications by Title
* Filter Notifications by Status

## Tech Stack

* FastAPI
* MySQL
* SQLAlchemy
* JWT Authentication
* Pydantic
* Uvicorn

## Installation

```bash
git clone <repository-url>
cd notification-service
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

DB_USER=root2
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=notification_db

SECRET_KEY=omix_secret_key_123

## Run Project

```bash
uvicorn app.main:app --reload
```

## API Documentation

Swagger UI:

http://127.0.0.1:8000/docs

## Author

Limisha Gorakhpuriya
