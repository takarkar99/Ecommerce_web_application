from django.db.models.signals import post_save
from django.dispatch import receiver
from CustomUser.models import CustomUser
from .models import Cart


@receiver(post_save, sender=CustomUser)
def post_save_create_user_cart(sender, instance, created, *args, **kwargs):
    if created:
        Cart.objects.create(CustomUser=instance)