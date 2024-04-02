from django.core.mail.backends.base import BaseEmailBackend


class HueyEmailBackend(BaseEmailBackend):
    def send_messages(self, email_messages):
        pass
