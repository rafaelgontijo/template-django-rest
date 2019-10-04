from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from .models import User
from .forms import UserChangeForm, UserCreationForm


@admin.register(User)
class UserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'name', 'date_joined', 'is_superuser', 'is_email_verified')
    list_filter = ('email', 'name', 'date_joined', 'is_superuser', 'is_email_verified')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('name', 'dob', 'cpf', 'gender', 'cellphone', 'is_email_verified')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2')}
         ),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['name', 'email', 'last_login', 'date_joined', 'is_email_verified']
        else:
            return ['last_login', 'date_joined', 'is_email_verified']
