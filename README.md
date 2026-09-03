# Notes App

A Django notes application for creating, organizing, and managing personal learning topics and journal entries.

## Live Demo

https://notes-app-gbwz.onrender.com

## About the Project

This app allows each user to:
- register for an account
- log in and log out securely
- create learning topics
- add detailed entries under each topic
- edit or update past notes
- only view their own topics and entries

The project includes user authentication, topic ownership, and protected access control so users can only manage their own content.

## Tech Stack

- Python
- Django 6.1.1
- SQLite for local development
- Gunicorn for production serving
- WhiteNoise for static files
- Render for deployment

## Project Structure

```bash
Notes-app/
├── README.md
├── render.yaml
├── learning_log/
│   ├── manage.py
│   ├── requirements.txt
│   ├── db.sqlite3
│   ├── staticfiles/
│   └── learning_log/
│       ├── __init__.py
│       ├── settings.py
│       ├── urls.py
│       ├── wsgi.py
│       └── asgi.py
│   ├── learning_logs/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── forms.py
│   │   ├── urls.py
│   │   └── templates/
│   └── users/
│       ├── views.py
│       ├── urls.py
│       └── templates/
└── .gitignore
```

## Features

- Topic-based notes organization
- Personal entries tied to each user
- User authentication and registration flow
- Protected access to private data
- Modern custom UI styling
- Deployment-ready Django configuration for Render

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/Subash-074/Notes-app.git
   cd Notes-app
   ```

2. Create and activate a virtual environment:
   ```bash
   py -m venv .venv
   .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r learning_log/requirements.txt
   ```

4. Apply migrations:
   ```bash
   cd learning_log
   python manage.py migrate
   ```

5. Run the app locally:
   ```bash
   python manage.py runserver
   ```

6. Open the app in the browser:
   ```text
   http://127.0.0.1:8000/
   ```

## Deployment

This project is configured for deployment on Render.

### Render settings

Build command:
```bash
pip install -r requirements.txt && python manage.py collectstatic --noinput
```

Start command:
```bash
gunicorn learning_log.wsgi:application --bind 0.0.0.0:$PORT
```

Environment variables:
```bash
DEBUG=False
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=notes-app-gbwz.onrender.com,localhost,127.0.0.1
```

## Status

- [x] Core app functionality
- [x] User authentication
- [x] Personal notes system
- [x] Deployment configuration
- [x] Live app available on Render
