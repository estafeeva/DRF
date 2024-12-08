import datetime

from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from config.settings import EMAIL_HOST_USER
from materials.models import Subscription
from users.models import User


@shared_task
def send_letter_updates_for_users(course_id):
    """
    Когда курс обновлен — тем, кто подписан на обновления именно этого курса,
    отправляется письмо на почту.
    """
    print(course_id)
    subscription_course = Subscription.objects.filter(course=course_id)
    for subscription in subscription_course:
        print(f"Отправить письмо на почту: {subscription.user.email}")
        send_mail(
            subject="Обновились данные курса",
            message=f"В курсе {subscription.course.name} произошли изменения.",
            from_email=EMAIL_HOST_USER,
            recipient_list=[subscription.user.email],
            fail_silently=True,
        )


@shared_task
def check_users():
    """
    Проверяет заходил ли пользователь в предыдущие 30 дней.
    И если не заходил, то блокирует его с помощью флага is_active
    """
    datetime_now = timezone.now()
    datetime_30_days_earlier = datetime_now - datetime.timedelta(days=30)

    users = User.objects.all()

    for user in users:
        if user.is_active:
            if user.last_login is None or user.last_login <= datetime_30_days_earlier:
                user.is_active = False
                user.save()

    print("Проверка выполнена")
