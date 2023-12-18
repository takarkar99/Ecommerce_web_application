from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin
from .models import Product, Cart, Order, Productincard


class ProductIncartInline(admin.TabularInline):
    model = Productincard


class CartInline(admin.TabularInline):
    model = Cart    #onetoonefield or foreignkey to dispay relation in Usermodels


class DealInline(admin.TabularInline): #many to many relation
    model = Order.CustomUser.through


# class Useradmin(UserAdmin):

#     model = User
#     list_display = ['username', 'get_card', 'is_staff', 'is_active']
#     list_filter = ['username', 'is_staff', 'is_active', 'is_superuser']
    
#     fieldsets = (
#         (None, {'fields' : ('username', 'password')}),
#         ('permissions', {'fields': ('is_staff',('is_active', 'is_superuser'))}),
#         ('important dates', {'fields': ('last_login','date_joined')}),
#         #('card', {'fields': ('get_card',)}),
#         ('advanced options', {
#             'classes': ('collapse',),
#             'fields' : ('groups', 'user_permissions')
#         }),
#     )

#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser', 'groups'),
#         }),
#     )

#     inlines = [
#         CartInline, DealInline
#     ]


#     def get_card(self, obj):
#         return obj.card


@admin.register(Cart)   
class CartAdmin(admin.ModelAdmin):

    model = Cart
    list_display = ('staff', 'CustomUser', 'created_on',) # here user__is_staff will not work
    readonly_fields = ['created_on']
    list_filter = ('CustomUser', 'created_on',)

    fieldsets = (
        (None, {'fields': ('CustomUser', 'created_on',)}), 
    )
    inlines  = (
        ProductIncartInline,
    )

    def staff(self, obj):
        return obj.CustomUser.is_staff


    staff.admin_order_field = 'CustomUser__is_staff'
    staff.short_description = 'staff CustomUser'

    list_filter = ['CustomUser__is_staff', 'created_on']


admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Productincard)


#admin.site.unregister(User)
#admin.site.register(User, Useradmin)