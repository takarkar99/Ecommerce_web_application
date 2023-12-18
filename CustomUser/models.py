from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .CustomManager import CustomManager



# class UserType(models.Model):
#     CUSTOMER = 1
#     SELLER = 3
#     TYPE_CHOICES = (
#         (SELLER, 'seller'),
#         (CUSTOMER, 'customer')
#     )

#     id = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, primary_key=True)

#     def __str__(self):
#         return self.get_id_display()
    
class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=250, verbose_name='email address' ,unique=True)
    name = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)
    date_of_birth = models.DateTimeField(default="1999-10-16")
    is_staff = models.BooleanField(default=True)

    # is_customer = models.BooleanField(default= True)
    # is_seller = models.BooleanField(default= False)
   
    # type = ( 
    #     (1, 'Seller'),
    #     (2, 'Customer')
    # )

    # user_type = models.IntegerField( choices=type, default=1)
    # userType = models.ManyToManyField(UserType)
    def __str__(self):
       return self.email

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['date_of_birth']

    objects = CustomManager()


    def save(self, *args, **kwargs):
       if not self.id:
          self.type = self.default_type
       return super().save(*args, **kwargs)
       

    class Types(models.TextChoices):
        SELLER = "seller", "SELLER"
        CUSTOMER = 'customer', 'CUSTOMER'


    default_type = Types.CUSTOMER

    type = models.CharField(('types'), max_length=250, choices=Types.choices, default=default_type)

     
class CustomerAddition(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=250)


class SellerAddition(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gst = models.CharField(max_length=10)
    warehouse_location = models.CharField(max_length=250)


class SellerManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type= CustomUser.Types.SELLER)
    

class CustomerManager(models.Manager):
   
   def get_queryset(self, *args, **kwargs):
      return super().get_queryset(*args, **kwargs).filter(type = CustomUser.Types.CUSTOMER)
   

class Seller(CustomUser):
   default_type = CustomUser.Types.SELLER
   objects = SellerManager()

   class Meta:
      proxy = True
      
   def sell(self):
      print('i can sell')
   
   @property
   def showadditional(self):
      return self.selleraddition
    

class Customer(CustomUser):
   default_type = CustomUser.Types.CUSTOMER
   objects = CustomerManager()

   class Meta:
      proxy = True

   def buy(self):
      print('I can Buy')
   
   @property
   def showadditional(self):
      return self.customaddition