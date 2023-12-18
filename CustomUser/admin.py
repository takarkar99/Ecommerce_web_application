from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import Usercreationforms, Userchangeforms
from .models import CustomUser, Customer, Seller


class Customadmin(UserAdmin):

    add_form = Usercreationforms
    form = Userchangeforms
    list_display = ('email','is_staff', 'date_of_birth',)
    list_filter = ('email', 'is_staff')
    # fields = ('email',)



    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('permissions', {'fields': ('is_staff', 'is_active',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, Customadmin)
# admin.site.register(UserType)

admin.site.register(Customer)
admin.site.register(Seller)