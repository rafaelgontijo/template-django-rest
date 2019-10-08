from django_filters import rest_framework as filters
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from .models import User
from .permissions import IsUserOrReadOnly
from .serializers import CreateUserSerializer, UserSerializer


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """
    List, updates and retrieves user accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser, IsUserOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = {
        'name': ('icontains',),
        'email': ('icontains',),
    }



class UserCreateViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    Creates user accounts
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)
