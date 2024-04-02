from django.conf import settings
from django.core.mail import get_connection
from django.core.mail.backends.base import BaseEmailBackend
from huey.contrib import djhuey


class HueyEmailBackend(BaseEmailBackend):
    def __init__(self, fail_silently=False, **kwargs):
        super().__init__(fail_silently)
        self.kwargs = kwargs

    def send_messages(self, email_messages):
        _ = _send_messages(
            email_messages,
            self.fail_silently,
            **self.kwargs,
        )
        return len(email_messages)


@djhuey.task()
def _send_messages(email_messages, fail_silently, **kwargs):
    backend = getattr(
        settings,
        "HUEY_EMAIL_BACKEND",
        "django.core.mail.backends.smtp.EmailBackend",
    )

    with get_connection(
        backend=backend,
        fail_silently=fail_silently,
        **kwargs,
    ) as conn:
        return conn.send_messages(email_messages)
