# ApiPamps

ApiPamps is a modern, scalable RESTful API built with **FastAPI**, **SQLAlchemy**, and **Alembic**, designed to provide a secure, modular, and production-ready foundation for application development.

## 🚀 Features
- 🔐 **Authentication & Authorization** (JWT-based)
- 👤 **User Management** (registration, login, profile)
- 📝 **Posts Management** (CRUD operations)
- 🗄️ **Database Migrations** with Alembic
- 🐳 **Docker & Docker Compose** support
- ✅ **Testing Suite** with Pytest
- ⚡ Built with **FastAPI** for high performance and async support

## 🛠️ Tech Stack
- [Python 3.12+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)

## 📂 Project Structure


ApiPamps/
│── pamps/ # Core application
│ ├── routes/ # API routes
│ ├── models/ # Database models
│ ├── auth.py # Authentication logic
│ ├── db.py # Database connection
│ └── ...
│── migrations/ # Alembic migrations
│── tests/ # Unit and integration tests
│── docker-compose.yml # Docker setup
│── requirements.txt # Project dependencies
│── setup.py # Package setup
│── README.md # Documentation




## ⚙️ Installation & Usage

### 1. Clone the repository

```bash
git clone https://github.com/DenilsonNatalito/ApiPamps.git
cd ApiPamps






python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt


DATABASE_URL=postgresql://user:password@localhost:5432/apipamps


alembic upgrade head



uvicorn pamps.app:app --reload
docker-compose up --build





