from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = '{{cookiecutter.app_name}}.users'
    verbose_name = _('App Users')
