# 🚀 FastAPI CRUD Application

A simple **CRUD (Create, Read, Update, Delete)** REST API built using **FastAPI**.
This project demonstrates how to build a backend API with request validation, database integration, and RESTful endpoints.

---

## 📌 Features

✅ Create new records
✅ Read all records or single record
✅ Update existing records
✅ Delete records
✅ Request validation using Pydantic
✅ Database integration (SQLAlchemy)
✅ Interactive API docs (Swagger UI)

---

## 🛠 Tech Stack

* FastAPI
* Python
* SQLAlchemy
* Pydantic
* Uvicorn
* SQLite / MySQL / PostgreSQL (configure as needed)

---

## 📂 Project Structure

```
project/
│
├── main.py              # FastAPI app entry point
├── database.py          # Database connection setup
├── models.py            # SQLAlchemy models
├── schemas.py           # Pydantic schemas
├── crud.py              # CRUD operations
├── requirements.txt     # Dependencies
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone repository

```
git clone https://github.com/yourusername/fastapi-crud-app.git
cd fastapi-crud-app
```

---

### 2️⃣ Create virtual environment

```
python -m venv venv
```

Activate environment:

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```
uvicorn main:app --reload
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

## 🔗 API Endpoints Example

| Method | Endpoint    | Description    |
| ------ | ----------- | -------------- |
| POST   | /items      | Create item    |
| GET    | /items      | Get all items  |
| GET    | /items/{id} | Get item by ID |
| PUT    | /items/{id} | Update item    |
| DELETE | /items/{id} | Delete item    |

---

## 🧪 Example Request (POST)

```
{
  "name": "Laptop",
  "price": 50000,
  "description": "Gaming laptop"
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
```

---

## 🚀 Future Improvements

* JWT Authentication
* User roles & permissions
* Pagination
* Docker deployment
* Unit testing
* CI/CD pipeline

---

## 👨‍💻 Author

Your Name
GitHub: https://github.com/yourusername

---

## 📄 License

This project is licensed under the MIT License.
