"""
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Upload

@receiver(post_save, sender=Upload)
def notify_owner_on_update(sender, instance, created, **kwargs):
    subject = "Database Update Notification"
    if created:
        message = f"A new upload was added:\nImage: {instance.image}\nDocument: {instance.document}"
    else:
        message = f"An existing upload was updated:\nImage: {instance.image}\nDocument: {instance.document}"

    send_mail(
        subject,
        message,
        'yourappowner@gmail.com',       # from
        ['yourappowner@gmail.com'],     # to (owner)
        fail_silently=False,
    )

"""