# Learning Log

A Django-based personal learning journal and notes platform designed with a modern social-feed interface inspired by Instagram.

## Live Demo

Local development:

https://notes-app-gbwz.onrender.com/
```

## About the Project

This app allows each user to:
- create an account and log in securely
- create their own learning topics
- write and update journal-style entries under each topic
- view only their personal notes in a social timeline layout
- edit entries directly from the dashboard
- experience a modern, minimal interface similar to social media apps

The project uses Django authentication and per-user ownership to keep each person’s content private and separate.

## Tech Stack

- Python
- Django 6.1.1
- SQLite for local development
- WhiteNoise for static file serving
- Gunicorn for production-ready deployment
- HTML, CSS, and JavaScript for the UI

## Project Structure

```bash
Notes-app/
├── README.md
├── learning_log/
│   ├── manage.py
│   ├── db.sqlite3
│   ├── learning_log/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   ├── learning_logs/
│   │   ├── migrations/
│   │   ├── static/
│   │   ├── templates/
│   │   ├── admin.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── users/
│       ├── templates/
│       ├── urls.py
│       ├── views.py
│       └── __init__.py
├── .gitignore
├── .venv/
├── render.yaml
└── requirements.txt
```

## Features

- User registration and login flow
- Private topic ownership per user
- Journal-style entries with edit support
- Instagram-inspired UI design
- Modern nav bar, cards, feed layout, and premium landing page
- Responsive layout for desktop and mobile screens
- Clean social dashboard experience for logged-in users

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
   pip install -r requirements.txt
   ```

4. Navigate to the Django project folder:
   ```bash
   cd learning_log
   ```

5. Apply migrations:
   ```bash
   python manage.py migrate
   ```

6. Run the app locally:
   ```bash
   python manage.py runserver
   ```

7. Open in your browser:
   ```text
   http://127.0.0.1:8000/
   ```

## Local Development Notes

- The app uses SQLite for development, which is convenient for local testing.
- Logged-in users are redirected to the personal social dashboard.
- Logged-out users see the public landing page and marketing-style home screen.
- Topics and entries are scoped to the currently authenticated user.

## Deployment

This project is deployment-ready for Django hosting platforms such as Render.

### Example Render setup

Build command:
```bash
pip install -r requirements.txt && python manage.py collectstatic --noinput
```

Start command:
```bash
gunicorn learning_log.wsgi:application --bind 0.0.0.0:$PORT
```

Recommended environment variables:
```bash
DEBUG=False
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=your-domain.com,localhost,127.0.0.1
```

## Status

- [x] User authentication
- [x] Personal notes and topic management
- [x] Social-style dashboard design
- [x] Edit functionality for entries
- [x] Responsive UI
- [x] Local Django app runs successfully
- [x] Project structure documented
