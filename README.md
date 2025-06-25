# Employee Management System

_A complete HR management solution with APIs, analytics dashboard, and secure access control._

---

## Project Overview

### Core Features
- **Employee lifecycle management**
  - Department assignment
  - Employment status tracking
  - Contact information storage
- **Time & Attendance**
  - Daily status tracking (Present/Absent/Late)
  - Monthly attendance analytics
- **Performance Management**
  - Quarterly reviews with ratings
  - Manager comments system
- **Data Visualization**
  - Interactive department distribution charts
  - Historical attendance trends

### Technical Highlights
- **Secure REST API** with JWT authentication
- **Auto-generated documentation** via Swagger/OpenAPI
- **PostgreSQL** database with Faker data seeding
- **Responsive dashboard** with Chart.js visualizations

**Tech Stack**: 
- Backend: Django 4, Django REST Framework
- Database: PostgreSQL
- Auth: JWT (SimpleJWT)
- Docs: drf-yasg
- Visualization: Chart.js

---

## Setup Instructions

### Prerequisites
- Python 3.10+
- PostgreSQL 14+
- Node.js 16+ (for chart rendering)
- Git

### 1. Initial Setup
```bash
# Clone repository
git clone https://github.com/your-repo/employee-management.git
cd employee-management

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows
```

### 2. Configure Environment
```bash
cp .env.example .env
```

Edit `.env` with your:
```ini
SECRET_KEY=your-django-secret-key
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
```bash
python manage.py migrate
python manage.py seed_data  
```

### 5. Run Development Server
```bash
python manage.py runserver
```
Access endpoints:
 - API: http://localhost:8000/api/
 - Admin: http://localhost:8000/admin/
 - Dashboard: http://localhost:8000/dashboard/

---

## API Usage Guide

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

| Endpoint                | Description                     |
|-------------------------|---------------------------------|
| `/api/employees/`       | Filter by department, status    |
| `/api/employees/{id}/`  | Name-based search               |
| `/api/attendance/`      | Date range filtering            |
| `/api/performance/`     | Rating-based sorting            |

### Example Queries

```http
GET /api/employees/?department=Engineering&employment_status=FT
GET /api/attendance/?date__year=2025&date__month=6
GET /api/performance/?rating__gte=3&ordering=-review_date
```

---

## Dashboard Features
### Acesss
http://localhost:8000/dashboard/

### Visualization Components
#### 1. Department Distribution
 - Real-time employee count by department
 - Interactive pie chart with hover details
#### 2. Attendance Analytics
 - Monthly present/absent trends
 - Configurable date ranges (last 6/12 months)

### Usage Tips
- Click chart legends to toggle data sets
- Hover over chart elements for detailed counts
- Refresh page to load latest data

---

## Documentation
### Interactive API Docs
- Swagger UI: http://localhost:8000/swagger/
- ReDoc: http://localhost:8000/redoc/

---

## Deployment
### TODO

---

## Project Structure
```text
employee_project/
├── employees/          # Core employee management
├── attendance/         # Time tracking system
├── employee_project/   # Configuration
├── templates/          # Dashboard views
├── tests/              # Unit and integration tests
└── management/         # Data seeding commands
