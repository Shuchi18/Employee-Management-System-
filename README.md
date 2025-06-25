# 📊 Employee Management System

_A Django REST API for managing employee data with JWT authentication and Swagger documentation._

---

## 🌟 Project Overview

A full-featured employee management system that includes:
- **Employee/department tracking** with relational databases
- **Attendance & performance records**
- **Secure REST APIs** with JWT authentication
- **Interactive documentation** via Swagger UI
- **Data visualization** (optional charts)

**Tech Stack**: Django 4 | PostgreSQL | DRF | SimpleJWT | drf-yasg | Chart.js

---

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.10+
- PostgreSQL 14+
- Node.js (for charts, optional)

### 1. Clone Repository
```bash
git clone https://github.com/your-repo/employee-management.git
cd employee-management
```

### 2. Configure Environment
```bash
cp .env.example .env
```
Edit `.env` with your:
```ini
DATABASE_URL=postgres://user:password@localhost:5432/employeedb
SECRET_KEY=your-django-secret-key
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
```bash
python manage.py migrate
python manage.py seed_data  # Optional: Loads 50 fake records
```

### 5. Run Development Server
```bash
python manage.py runserver
```
Access at: [http://localhost:8000](http://localhost:8000)

---

## 🔌 API Usage Guide

### Authentication

1. Get JWT tokens:
   ```bash
   curl -X POST http://localhost:8000/api/token/ \
   -H "Content-Type: application/json" \
   -d '{"username":"admin", "password":"yourpassword"}'
   ```

   Response:
   ```json
   {
     "refresh": "xxxxx",
     "access": "xxxxx"
   }
   ```

2. Use in requests:
   ```bash
   curl -H "Authorization: Bearer xxx.yyy.zzz" \
   http://localhost:8000/api/employees/
   ```

### Key Endpoints

| Endpoint                | Methods | Description                     |
|-------------------------|---------|---------------------------------|
| `/api/employees/`       | GET,POST| List/create employees           |
| `/api/employees/{id}/`  | ALL     | Manage specific employee        |
| `/api/attendance/`      | GET,POST| Filterable attendance records   |
| `/api/performance/`     | GET,POST| Employee performance reviews    |

### Filtering Examples

```http
GET /api/employees/?department=1
GET /api/attendance/?date__gte=2025-01-01&status=P
```

---

## 📚 Documentation

**Interactive API Explorer**:  
[http://localhost:8000/swagger/](http://localhost:8000/swagger/)

![Swagger UI Preview](https://i.imgur.com/JQ8W5Vp.png)

---

## 🚀 Deployment

### Docker (Recommended)
```bash
docker-compose up -d
```
Access: [http://localhost:8001](http://localhost:8001)

### Cloud Platforms

[![Deploy on Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

---
