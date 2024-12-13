from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail

from website_shop import settings
from .views import Order


@receiver(post_save, sender=Order)
def order_save(sender, instance, created, **kwargs):
    if created:
        subject = 'My_Books_Shop'
        message = f'Привет, {instance.user}! Ваш заказ номер: {instance.number}  \
                    находиться в статусе: {instance.status}.'

        from_email = settings.EMAIL_HOST_USER
        to_email = instance.email
        send_mail(
            subject,
            message,
            from_email,
            [to_email],
            fail_silently=False,
        )
