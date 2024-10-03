from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework.decorators import permission_classes
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView

from accounts.api.serializers import UserSerializer
from accounts.api.filters import UserFilter

from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

from base.helpers.decorators import exception_handler
from base.permissions import IsStaff, IsSuperUser

User = get_user_model()


class UserProfileRetrieveUpdateView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.filter()
    http_method_names = ['get', 'patch']
    swagger_tags = ['User Profile']

    def get_object(self):
        return self.request.user

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


class AdminUserListCreateApiView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, (IsStaff | IsSuperUser),)
    serializer_class = UserSerializer
    queryset = User.objects.filter()
    filterset_class = UserFilter
    swagger_tags = ['Users']

    @method_decorator(exception_handler)
    def create(self, request, *args, **kwargs):
        request.data['is_active'] = True
        request.data['password'] = make_password(request.data['password'])
        return super(AdminUserListCreateApiView, self).create(request, *args, **kwargs)



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['full_name'] = user.full_name
        token['role'] = user.role.name if user.role else ""
        token['role_key'] = user.role.key if user.role else ""
        token['email'] = user.email
        token['contact_number'] = user.contact_number
        return token

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer