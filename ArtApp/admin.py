from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import Cart, Artist, ArtPiece, Order, Category, CustomUser, DeliveryInfo

# Register your models here.
class ArtAdmin(admin.ModelAdmin):
    pass 
admin.site.register(ArtPiece, ArtAdmin)

class ArtistAdmin(admin.ModelAdmin):
    pass 
admin.site.register(Artist, ArtistAdmin)

class CategoryAdmin(admin.ModelAdmin):
    pass 
admin.site.register(Category, CategoryAdmin)

class CartAdmin(admin.ModelAdmin):
    pass 
admin.site.register(Cart, CartAdmin)

class DeliveryInfoAdmin(admin.ModelAdmin):
    pass 
admin.site.register(DeliveryInfo, DeliveryInfoAdmin)

class OrderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Order, OrderAdmin)

class CustomUserCreationForm(UserCreationForm):
    role=forms.ChoiceField(choices=CustomUser.ROLE_CHOICES)

    class Meta(UserCreationForm.Meta):
        model=CustomUser
        fields=UserCreationForm.Meta.fields+('role',)

class CustomUserAdmin(UserAdmin):
    list_display=('username', 'email', 'first_name', 'last_name', 'is_staff', 'role',)
    fieldsets=(
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'
            )
        }), 
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields':('role',)
        })
    )
    add_fieldsets=(
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('User Roles', {
            'fields': ('role', )
        })
    )
    add_form=CustomUserCreationForm

admin.site.register(CustomUser, CustomUserAdmin)

