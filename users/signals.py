from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail


from website_shop import settings

User = get_user_model()

@receiver(post_save, sender=User)
def user_postsave(sender, instance, created, **kwargs):
    if created:
        subject = instance.first_name
        message = f'Привет, {instance.first_name}! Рады видеть!'
        from_email = settings.EMAIL_HOST_USER
        to_email = instance.email
        send_mail(
            subject,
            message,
            from_email,
            [to_email],
            fail_silently=False,
        )
