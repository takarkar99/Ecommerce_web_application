from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class Usercreationforms(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email",)


class Userchangeforms(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)