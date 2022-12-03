
from django.core.mail import send_mail
from django.conf import settings


def SendEmail():

    subject = 'Welcome to DevSearch'
    message = 'We are glad you are here'

    send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            ["mbarozzi@gmail.com"],
            fail_silently=False,
            )
