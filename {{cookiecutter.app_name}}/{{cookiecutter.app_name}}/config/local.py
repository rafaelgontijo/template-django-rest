import os
from .common import Common
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Local(Common):
    DEBUG = True

    # Testing
    INSTALLED_APPS = Common.INSTALLED_APPS

    # Mail
    EMAIL_HOST = 'mailhog'
    EMAIL_PORT = 1025
    EMAIL_USE_TLS = False

    CORS_ORIGIN_ALLOW_ALL = True
