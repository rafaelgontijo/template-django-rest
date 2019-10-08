from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import(
    obtain_jwt_token, refresh_jwt_token, verify_jwt_token
)
from .docs.views import schema_view
from .users.views import UserViewSet, UserListCreateViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'users', UserListCreateViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api-token-auth/', obtain_jwt_token, name='api-token-auth'),
    path('api-token-refresh/', refresh_jwt_token, name='api-token-refresh'),
    path('api-token-verify/', verify_jwt_token, name='api-token-verify'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('doc<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
