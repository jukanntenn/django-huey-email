# django-huey-email

Asynchronous Email Backend for [Django](https://www.djangoproject.com/) with [Huey](https://github.com/coleifer/huey).

## Requirements

Python: >=3.8, <4

Django: >=3.2, <6.0

## Installation

```bash
pip install django-huey-email
```

## Usage

Set `django-huey-email` as your email backend:

```python
EMAIL_BACKEND = "huey_email.backends.HueyEmailBackend"
```

By default, `django-huey-email` utilizes Django's built-in SMTP email backend for the actual email sending process. If you prefer to use a different backend, you can specify this by setting the `HUEY_EMAIL_BACKEND` in your settings. For instance, to use Django's console email backend instead, configure the settings as follows:

```python
EMAIL_BACKEND = "huey_email.backends.HueyEmailBackend"
HUEY_EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
```
