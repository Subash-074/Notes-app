# Notes App

A Django web application that lets users log the topics they are learning about and record what they've learned about each one.

## About the Project

This is a Notes Taking app where each user can:
- Register for an account and log in / log out
- Create personal **topics** they want to save
- Add **entries** (notes) under each topic describing what they've learned
- Edit existing entries
- View only their own topics and entries (other users' data is kept private)

User accounts are fully implemented — registration, login, logout, and access control so users can only see and edit their own topics and entries. Styling the app, and deployment is currently in progress.

> **Note:** Deployment has **not** been done yet. The project currently runs locally only.

## Tech Stack

- **Python**
- **Django** (6.0.7)
- **SQLite** (default local database)
- HTML / CSS (Django templates)

## Project Structure

```
learning_log/
├── manage.py
├── db.sqlite3
├── learning_log/          # Project settings, URLs, WSGI/ASGI config
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── learning_logs/         # Main app: topics & entries
│   ├── models.py          # Topic and Entry models
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/learning_logs/
└── users/                 # User accounts app: register, login, logout
    ├── views.py
    ├── urls.py
    └── templates/users/
```

## Features

- **Topics & Entries** – Each `Topic` belongs to a user (`owner`), and each `Entry` belongs to a `Topic`. Topics and entries are only visible to the user who created them.
- **User Authentication** – Registration, login, and logout pages under the `users` app.
- **Access Control** – Views are protected with `@login_required`, and users attempting to view or edit topics/entries that aren't theirs receive a 404.

## Getting Started

1. Clone the repository and navigate to the project folder:
   ```bash
   git clone https://github.com/Subash-074/Notes-app.git
   cd Notes-app/learning_log
   ```
2. (Recommended) Create and activate a virtual environment:
   ```bash
   python -m venv ll_env
   source ll_env/bin/activate   # On Windows: ll_env\Scripts\activate
   ```
3. Install Django:
   ```bash
   pip install django
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser (optional, for the admin site):
   ```bash
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```
7. Open your browser at `http://localhost:8000/`.

## Status / Roadmap

- [x] Core app: topics and entries (models, views, templates)
- [x] User accounts: register, login, logout, restricted access
- [ ] Styling the app (in progress)
- [ ] Deployment (not yet done)
