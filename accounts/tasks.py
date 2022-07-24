from celery import shared_task
from django.contrib.auth import get_user_model

from accounts.api.utils import send_email

CustomUser = get_user_model()


@shared_task
def send_email_task(user_id, email_type):
    user = CustomUser.objects.get(id=user_id)
    send_email(user, email_type)
