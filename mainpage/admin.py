from django.contrib import admin
from .models import CustomUser
from .forms import SignUpForm, UserChangeForm
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = SignUpForm

    list_display = ('username','is_active','is_superuser')
    list_filter = ('is_active',)
    fieldsets = (
        ('Account info', {'fields': ('username','password')}),
        ('Personal info', {'fields': ('name','birth','gender','belong','position','address','email','phone','finalEducation','major')}),
        ('Permissions', {'fields': ('is_active','is_superuser')}),
    )
    # # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','name', 'birth','gender', 'password1', 'password2'),
        }),
    )
    search_fields = ('name','username')
    ordering = ('is_active',)
    filter_horizontal = ()

admin.site.register(CustomUser,UserAdmin)
admin.site.unregister(Group)