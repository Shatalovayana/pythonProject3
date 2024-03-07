from celery import shared_task
from django.core.mail import send_mail

from config import settings


@shared_task
def update_material_mail(email):
    send_mail(
        subject='Обновление материалов курса',
        message='У нас произошли обновления в материалах курса',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )
