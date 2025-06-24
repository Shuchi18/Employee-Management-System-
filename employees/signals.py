from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from rolepermissions.roles import assign_role


@receiver(post_save, sender=User)
def set_user_role(sender, instance, created, **kwargs):
    if created:
        if instance.is_superuser:
            assign_role(instance, 'Admin')
        elif instance.email.endswith('@company.com'):
            assign_role(instance, 'HR')
        else:
            assign_role(instance, 'Employee')
