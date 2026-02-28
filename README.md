# 🎓 CampusInsight360

## 📋 Overview

**CampusInsight360** is a comprehensive Campus Resource Management System built with Django that provides intelligent insights and analytics for managing campus infrastructure, faculty, courses, and students. The system helps educational institutions optimize their resource utilization through data-driven decision-making.

## 🌟 Key Features

### 1. **Campus Block Management**
- Track and manage multiple campus blocks
- Monitor total classrooms and maximum capacity per block
- Calculate real-time capacity utilization percentages
- View current vs maximum capacity metrics

### 2. **Classroom Management**
- Organize classrooms by campus blocks
- Track seating capacity for each classroom
- Monitor student occupancy in real-time
- Calculate classroom utilization percentages
- Prevent overcrowding with capacity tracking

### 3. **Faculty Management**
- Maintain faculty profiles with department information
- Track teaching load and maximum workload limits
- Monitor workload distribution across faculty
- Calculate workload percentages for balanced assignment
- Prevent faculty overload with automated tracking

### 4. **Course Management**
- Create and manage courses with unique course codes
- Assign faculty members to courses
- Allocate classrooms for each course
- Track credit hours and course requirements
- Monitor student enrollment per course

### 5. **Student Management**
- Maintain student records with unique registration numbers
- Assign students to courses and classrooms
- Track student distribution across campus
- Monitor enrollment statistics

### 6. **Analytics Dashboard**
- **Block Utilization Analytics**: View capacity usage across all campus blocks
- **Classroom Occupancy Reports**: Track which classrooms are over/under-utilized
- **Faculty Workload Distribution**: Identify overburdened or underutilized faculty
- **Student Distribution**: Analyze student enrollment patterns across courses
- **Real-time Metrics**: Get instant insights on all campus resources

### 7. **User Authentication**
- Secure login system
- Role-based access control
- Protected routes for authorized users only
- Session management

## 🛠️ Tech Stack

### Backend
- **Framework**: Django 6.0.2
- **Language**: Python 3.x
- **Database**: PostgreSQL (production) / SQLite3 (development)
- **Authentication**: Django built-in authentication system

### Frontend
- **Template Engine**: Django Templates
- **Styling**: HTML5, CSS3
- **Layout**: Responsive design with sidebar navigation

## 📊 Database Schema

### Models Overview

#### 1. **CampusBlock Model**
```python
- name (CharField): Unique block identifier
- total_classrooms (PositiveIntegerField): Number of classrooms
- max_capacity (PositiveIntegerField): Maximum student capacity
- Methods:
  - current_capacity(): Calculates total seating across all classrooms
  - utilization_percentage(): Returns capacity usage percentage
```

#### 2. **Classroom Model**
```python
- name (CharField): Classroom identifier
- block (ForeignKey to CampusBlock): Parent block
- seating_capacity (PositiveIntegerField): Maximum seats
- Methods:
  - current_students_count(): Number of enrolled students
  - utilization_percentage(): Returns occupancy percentage
```

#### 3. **Faculty Model**
```python
- name (CharField): Faculty member name
- department (CharField): Department affiliation
- max_teaching_load (PositiveIntegerField): Maximum teaching hours
- Methods:
  - current_teaching_load(): Sum of credit hours from assigned courses
  - workload_percentage(): Returns workload distribution percentage
```

#### 4. **Course Model**
```python
- name (CharField): Course name
- course_code (CharField): Unique course identifier
- credit_hours (PositiveIntegerField): Course credit value
- faculty (ForeignKey to Faculty): Assigned instructor
- classroom (ForeignKey to Classroom): Assigned location
- Methods:
  - enrolled_students_count(): Number of enrolled students
```

#### 5. **Student Model**
```python
- name (CharField): Student name
- registration_number (CharField): Unique student ID
- course (ForeignKey to Course): Enrolled course
- classroom (ForeignKey to Classroom): Assigned classroom
```

## 📁 Project Structure

```
CampusInsight360/
├── campus360/
│   ├── backend_360/              # Main Django app
│   │   ├── management/           # Django management commands
│   │   ├── migrations/           # Database migrations
│   │   ├── static/               # Static files
│   │   │   └── css/             # Stylesheets
│   │   ├── templates/           # HTML templates
│   │   │   ├── analytics.html   # Analytics dashboard
│   │   │   ├── base.html        # Base template with sidebar
│   │   │   ├── blocks.html      # Block management page
│   │   │   ├── classrooms.html  # Classroom management
│   │   │   ├── courses.html     # Course management
│   │   │   ├── faculty.html     # Faculty management
│   │   │   ├── index.html       # Dashboard homepage
│   │   │   ├── login.html       # Login page
│   │   │   └── students.html    # Student management
│   │   ├── __init__.py
│   │   ├── admin.py             # Django admin configuration
│   │   ├── apps.py              # App configuration
│   │   ├── models.py            # Database models
│   │   ├── tests.py             # Unit tests
│   │   ├── urls.py              # URL routing
│   │   └── views.py             # View functions
│   ├── campus360/               # Project configuration
│   │   ├── __init__.py
│   │   ├── asgi.py              # ASGI configuration
│   │   ├── settings.py          # Project settings
│   │   ├── urls.py              # Main URL configuration
│   │   └── wsgi.py              # WSGI configuration
│   ├── db.sqlite3               # SQLite database (development)
│   └── manage.py                # Django management script
├── .gitattributes
└── README.md                     # Project documentation
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- PostgreSQL 12 or higher (for production)
- pip (Python package manager)
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/sandeepkumar9760/CampusInsight360.git
cd CampusInsight360
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
cd campus360
pip install django
pip install psycopg2-binary  # For PostgreSQL support
```

### Step 4: Database Configuration

#### Option A: Using PostgreSQL (Recommended for Production)

1. Install and start PostgreSQL
2. Create a database:

```sql
CREATE DATABASE campus_dbs;
CREATE USER postgres WITH PASSWORD '123';
GRANT ALL PRIVILEGES ON DATABASE campus_dbs TO postgres;
```

3. Update `campus360/settings.py` (already configured):

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'campus_dbs',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

#### Option B: Using SQLite (Development Only)

Update `campus360/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### Step 5: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### Step 7: Run Development Server

```bash
python manage.py runserver
```

The application will be available at: **http://127.0.0.1:8000/**

## 🔐 Default Login

After creating a superuser, use those credentials to log in at:

```
URL: http://127.0.0.1:8000/
Username: [your_superuser_username]
Password: [your_superuser_password]
```

## 📱 Application Routes

| Route | View | Description |
|-------|------|-------------|
| `/` | Login View | User authentication page |
| `/dashboard/` | Dashboard | Main dashboard with statistics |
| `/blocks/` | Blocks View | Manage campus blocks |
| `/classrooms/` | Classrooms View | Manage classrooms |
| `/courses/` | Courses View | Manage courses |
| `/faculty/` | Faculty View | Manage faculty members |
| `/students/` | Students View | Manage student records |
| `/analytics/` | Analytics View | Resource utilization analytics |
| `/logout/` | Logout | End user session |

## 💡 Usage Guide

### 1. Initial Setup
1. Log in with superuser credentials
2. Navigate to **Blocks** and create campus blocks
3. Add **Classrooms** to each block
4. Create **Faculty** profiles
5. Set up **Courses** with assigned faculty and classrooms
6. Add **Students** and enroll them in courses

### 2. Dashboard Features
- View total counts of blocks, classrooms, courses, faculty, and students
- Quick navigation to all management pages
- Real-time statistics updates

### 3. Analytics Insights
- Monitor block capacity utilization
- Identify underutilized or overutilized classrooms
- Track faculty workload distribution
- Analyze student enrollment patterns
- Make data-driven decisions for resource allocation

## 🎯 Use Cases

### For Campus Administrators
- Optimize classroom allocation based on utilization data
- Ensure balanced faculty workload distribution
- Monitor campus capacity and plan expansions
- Track resource efficiency metrics

### For Academic Planning
- Assign appropriate classroom sizes based on enrollment
- Prevent faculty overload with workload tracking
- Optimize course scheduling and room assignments
- Analyze enrollment trends for better planning

### For Resource Management
- Identify unused or underutilized spaces
- Maximize campus infrastructure efficiency
- Generate reports for stakeholder meetings
- Support data-driven budget allocation

## 🔒 Security Features

- **Login Required Decorators**: All sensitive views require authentication
- **CSRF Protection**: Django's built-in CSRF middleware enabled
- **Password Validation**: Enforced password strength requirements
- **Session Management**: Secure session handling
- **SQL Injection Protection**: Django ORM prevents SQL injection

## ⚠️ Important Notes

1. **Secret Key**: Change the `SECRET_KEY` in `settings.py` before deploying to production
2. **Debug Mode**: Set `DEBUG = False` in production
3. **Allowed Hosts**: Configure `ALLOWED_HOSTS` for production deployment
4. **Database Credentials**: Update PostgreSQL credentials in production
5. **Static Files**: Run `python manage.py collectstatic` for production

## 🚧 Future Enhancements

- [ ] Add data visualization charts for analytics
- [ ] Implement export functionality (CSV, PDF)
- [ ] Add email notifications for capacity alerts
- [ ] Create mobile-responsive interface
- [ ] Integrate calendar view for course scheduling
- [ ] Add role-based permissions (admin, faculty, viewer)
- [ ] Implement advanced search and filtering
- [ ] Add bulk import/export for student data
- [ ] Create RESTful API for external integrations
- [ ] Add automated reporting system

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open-source and available for educational and commercial use.

## 👤 Author

**Sandeep Kumar**
- GitHub: [@sandeepkumar9760](https://github.com/sandeepkumar9760)
- LinkedIn: [Connect with me](https://www.linkedin.com/in/sandeep_kumar_ds)

## 🙏 Acknowledgments

- Built with Django framework
- Inspired by real-world campus management challenges
- Designed for scalability and ease of use

## 📞 Support

For questions, issues, or suggestions:
- Open an issue on GitHub
- Contact via email: [sandeepkumar270724@gmail.com]

---

**Made with ❤️ for better campus resource management**
