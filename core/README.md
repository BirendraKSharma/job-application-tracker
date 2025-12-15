# Django Mini Web Application

A simple Django web app demonstrating authentication, CRUD operations, search/filtering, and PDF generation.

## Features
- User signup, login, logout
- Secure authentication (Django auth)
- CRUD for Job Applications
- Search and status filtering
- PDF download of job records
- Admin panel support

## Tech Stack
- Django
- SQLite
- Django Templates (HTML)
- ReportLab (PDF)

## Run Locally
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
