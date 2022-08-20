import random
import string

from django.core.mail import send_mail

SIZE_CODE = 6


def send_mail_to_user(email, confirmation_code):
    send_mail(
        subject='Регистрация на Yamdb, код подтверждения',
        message='Спасибо за регистрацию в нашем сервисе. '
                f'Код подтверждения: {confirmation_code}',
        from_email='register@yambd.com',
        recipient_list=[email],
        fail_silently=False,
    )


def generate_confirmation_code():
    generate_pass = ''.join(
            random.choice(
                string.ascii_uppercase + string.digits,
            ) for n in range(SIZE_CODE)
    )
    return generate_pass
