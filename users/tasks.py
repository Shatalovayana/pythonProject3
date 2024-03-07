import datetime

from celery import shared_task
from django.utils import timezone

from users.models import User


@shared_task
def check_last_login():
    time_difference = datetime.datetime.now(timezone.utc) - datetime.timedelta(days=30)
    users_deactivated = User.objects.filter(last_login__lt=time_difference, is_active=True)
    users_deactivated.update(is_active=False)

