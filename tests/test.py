from django.core import mail
from django.core.mail import EmailMessage, get_connection
from django.test import SimpleTestCase, override_settings


class HueyEmailTestCase(SimpleTestCase):
    def test_send_email(self):
        # Django’s test runner automatically uses `locmem.EmailBackend`` for testing.
        # So we need to overide to use `HueyEmailBackend`.
        with override_settings(EMAIL_BACKEND="huey_email.backends.HueyEmailBackend"):
            self.assertEqual(len(mail.outbox), 0)
            with get_connection() as conn:
                msg1 = EmailMessage("msg1")
                msg2 = EmailMessage("msg2")
                conn.send_messages([msg1, msg2])

            self.assertEqual(len(mail.outbox), 2)
