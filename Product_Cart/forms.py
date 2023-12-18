from .models import Productincard
from django import forms


class cardform(forms.ModelForm):
    class Meta:
        model = Productincard
        fields = ['quantity',] 