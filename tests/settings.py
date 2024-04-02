SECRET_KEY = "test-secret-key"
HUEY_EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
HUEY = {
    "huey_class": "huey.MemoryHuey",
    "name": "huey-email",
    "immediate": True,
}
