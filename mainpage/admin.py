from django.contrib import admin
from .models import CustomUser
from .forms import SignUpForm, UserChangeForm
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = SignUpForm

    list_display = ('name','is_superuser')
    list_filter = ('is_superuser',)
    fieldsets = (
        ('Account info', {'fields': ('username','password')}),
        ('Personal info', {'fields': ('name','birth','gender')}),
        ('Permissions', {'fields': ('is_active','is_staff','is_admin','is_superuser')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','name', 'birth','gender', 'password1', 'password2'),
        }),
    )
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ()

admin.site.register(CustomUser)
admin.site.unregister(Group)