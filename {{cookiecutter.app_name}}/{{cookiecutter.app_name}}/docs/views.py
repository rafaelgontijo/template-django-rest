from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="{{cookiecutter.app_name}}",
        default_version='v1',
        description="{{cookiecutter.description}}",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="{{cookiecutter.email}}"),
        license=openapi.License(name="{{cookiecutter.license}}"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
