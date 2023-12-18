from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _ 


class CustomManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError("Email Must Be set")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)


        if extra_fields.get("is_staff") is not True:
            raise ValueError("super user must be is_staff True")
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("super user must be is_super True")

        
        return self.create_user(email, password, **extra_fields)