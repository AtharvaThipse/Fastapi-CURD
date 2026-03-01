# 🚀 FastAPI Blog CRUD API

A **FastAPI-based Blog CRUD application** with **JWT authentication**, **user management**, and **database integration** using SQLAlchemy.

This project demonstrates a clean backend architecture with separated **routers**, **repository layer**, and **authentication system**.

---

## 📌 Features

✅ User registration and login
✅ JWT token authentication
✅ Password hashing (secure storage)
✅ Blog CRUD operations
✅ Protected routes with OAuth2
✅ SQLAlchemy ORM integration
✅ SQLite database
✅ Modular project structure
✅ Interactive API documentation (Swagger UI)

---

## 🛠 Tech Stack

* Python
* FastAPI
* SQLAlchemy
* Pydantic
* Passlib (bcrypt)
* JWT Authentication
* Uvicorn
* SQLite

---

## 📂 Project Structure

```
FASTAPI TUTORIAL/
│
├── blog/
│   │
│   ├── repository/           # Database logic (CRUD operations)
│   │   ├── blog.py
│   │   └── user.py
│   │
│   ├── routers/              # API route handlers
│   │   ├── authentication.py
│   │   ├── blog.py
│   │   └── user.py
│   │
│   ├── database.py           # Database connection
│   ├── models.py             # SQLAlchemy models
│   ├── schema.py             # Pydantic schemas
│   ├── hashing.py            # Password hashing logic
│   ├── oauth2.py             # OAuth2 dependency
│   ├── token.py              # JWT token creation/verification
│   ├── main.py               # FastAPI app entry
│   └── blog.db               # SQLite database
│
├── requirements.txt          # Project dependencies
├── main.py                   # Root app runner (if used)
└── .gitignore
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/yourusername/fastapi-blog-crud.git
cd fastapi-blog-crud
```

---

### 2️⃣ Create virtual environment

```
python -m venv blog-env
```

Activate environment:

**Windows**

```
blog-env\Scripts\activate
```

**Mac/Linux**

```
source blog-env/bin/activate
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```
uvicorn blog.main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

## 📖 API Documentation

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

## 🔐 Authentication Flow

1. Register a user
2. Login using credentials
3. Receive JWT access token
4. Use token in headers:

```
Authorization: Bearer <your_token>
```

5. Access protected routes

---

## 🔗 API Endpoints

### 🔑 Authentication

| Method | Endpoint | Description   |
| ------ | -------- | ------------- |
| POST   | /login   | User login    |
| POST   | /user    | Register user |

---

### 📝 Blog

| Method | Endpoint   | Description    |
| ------ | ---------- | -------------- |
| POST   | /blog      | Create blog    |
| GET    | /blog      | Get all blogs  |
| GET    | /blog/{id} | Get blog by ID |
| PUT    | /blog/{id} | Update blog    |
| DELETE | /blog/{id} | Delete blog    |

---

## 🧪 Example Login Request

```
{
  "username": "test@gmail.com",
  "password": "1234"
}
```

---

## 📦 Requirements

Example `requirements.txt`:

```
fastapi
uvicorn
sqlalchemy
pydantic
passlib[bcrypt]
python-jose
```

---

## 🚀 Future Improvements

* Refresh tokens
* Role-based access control
* Pagination
* Docker deployment
* PostgreSQL integration
* Unit testing
* CI/CD pipeline

---

## 👨‍💻 Author

Atharva Thipse

---

## 📄 License

This project is licensed under the MIT License.
