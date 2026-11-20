# Django CRM

A Django-based customer record management application for creating and maintaining categorized member records.

## Features

- User registration and login
- Authenticated dashboard
- Create, view, update, and delete records
- Search records by first name, last name, or phone number
- Record categories
- Django admin support
- Responsive Bootstrap templates
- Custom 404 page

## Record Fields

- First name
- Last name
- Category
- Phone number
- Height
- Weight
- Address
- Creation date

## Tech Stack

- Python
- Django 6.1
- SQLite
- Django authentication
- Bootstrap 5
- django-crispy-forms
- Bootstrap 5 crispy forms

## Project Structure

```text
crm-project-django/
├── main_crm/          # Django project settings and URL configuration
├── webapp/            # CRM application models, views, forms, and routes
├── templates/
│   ├── base.html      # Shared page layout
│   ├── components/    # Navbar, alerts, and reusable records table
│   └── web/           # Application pages
├── db.sqlite3         # Local SQLite database
└── manage.py          # Django management utility
```

## Application Routes

| Route | Name | Purpose |
| --- | --- | --- |
| `/` | `home` | Landing page |
| `/register/` | `register` | Create an account |
| `/my-login/` | `login` | Sign in |
| `/dashboard/` | `dashboard` | View all records |
| `/logout/` | `logout` | Sign out |
| `/create-record/` | `create_record` | Add a record |
| `/view-record/<id>/` | `view_record` | View a record |
| `/update-record/<id>/` | `update_record` | Edit a record |
| `/delete-record/<id>/` | `delete_record` | Remove a record |
| `/search-records/` | `search_records` | Search records |
| `/admin/` | Django admin | Manage users and CRM data |

## Setup

Create and activate a virtual environment, install Django and the required template packages, then apply migrations:

```bash
python -m venv env
env\Scripts\activate
pip install django django-crispy-forms crispy-bootstrap5
python manage.py migrate
python manage.py runserver
```

The development server will be available at `http://127.0.0.1:8000/`.

## Development Notes

- Dashboard, record creation, record details, record updates, and record deletion require authentication.
- The project uses SQLite by default.
- Templates are loaded from the top-level `templates/` directory.
- `Category` and `Record` are registered in the Django admin.
- `DEBUG` is currently disabled in project settings.
