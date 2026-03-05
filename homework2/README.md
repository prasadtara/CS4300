# Movie App (Django + DRF)

Live Deployment:\
https://homework2-movieapp.onrender.com/movies/

This project is a **Django REST API** for managing movies. The
application is deployed on **Render** and uses **PostgreSQL in
production**.

------------------------------------------------------------------------

# Tech Stack

-   Django 4.2.28
-   Django REST Framework
-   Gunicorn
-   dj-database-url
-   psycopg2-binary
-   WhiteNoise (brotli)
-   Render (deployment)

------------------------------------------------------------------------

# Requirements

-   Python 3.10+
-   pip
-   virtualenv (recommended)

Dependencies are listed in:

    requirements.txt

Contents:

    Django==4.2.28
    djangorestframework
    gunicorn
    dj-database-url
    psycopg2-binary
    whitenoise[brotli]

------------------------------------------------------------------------

# Setup Instructions

## 1. Clone the Repository

``` bash
git clone <your-repository-url>
cd <project-folder>
```

------------------------------------------------------------------------

## 2. Create Virtual Environment

Linux / macOS:

``` bash
python -m venv venv
source venv/bin/activate
```

Windows:

``` bash
python -m venv venv
venv\Scripts\activate
```

------------------------------------------------------------------------

## 3. Install Dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## 4. Apply Migrations

``` bash
python manage.py migrate
```

------------------------------------------------------------------------

## 5. Run Development Server

``` bash
python manage.py runserver
```

Open the app in your browser:

    http://127.0.0.1:8000/movies/

------------------------------------------------------------------------

# Production Deployment (Render)

The project is deployed using **Gunicorn** and **Render**.

### Build Command

    pip install -r requirements.txt
    python manage.py collectstatic --noinput
    python manage.py migrate

### Start Command

    gunicorn project_name.wsgi:application

Replace:

    project_name

with the name of your Django project folder (the folder containing
`settings.py`).

------------------------------------------------------------------------

# Environment Variables

Typical environment variables used in production:

    SECRET_KEY=your_secret_key
    DEBUG=False
    ALLOWED_HOSTS=homework2-movieapp.onrender.com
    DATABASE_URL=your_database_url

Render usually provides the **DATABASE_URL** automatically if a
PostgreSQL service is attached.

------------------------------------------------------------------------

# API Endpoint

Example endpoint:

    GET /movies/

Live API:

    https://homework2-movieapp.onrender.com/movies/

------------------------------------------------------------------------

# Admin Access (Optional)

Create an admin user:

``` bash
python manage.py createsuperuser
```

Then visit:

    http://127.0.0.1:8000/admin/

------------------------------------------------------------------------

# Static Files

Static files are handled using **WhiteNoise** in production.

Collect static files:

``` bash
python manage.py collectstatic
```

------------------------------------------------------------------------

# License

This project is for educational purposes.
