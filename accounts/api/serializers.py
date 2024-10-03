from base.serializers import DynamicFieldsModelSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from accounts.models import Role


User = get_user_model()


class RoleSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name', 'key') 


class UserSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'role', 'full_name', 'username', 'password', 'email', 'contact_number')

    