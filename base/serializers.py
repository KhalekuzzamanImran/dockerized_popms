from rest_framework.serializers import SerializerMethodField, ModelSerializer
from django.contrib.auth import get_user_model
from base.models import BaseModel

User = get_user_model()

class DynamicFieldsModelSerializer(ModelSerializer):
    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)
        method_fields = kwargs.pop('method_fields', None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)
        if fields:
            fields = fields.split(',')
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

        if method_fields:
            method_fields = method_fields.split(',')
            for name in method_fields:
                self.fields[name] = SerializerMethodField(
                    read_only=True, source=f'get_{name}')


class UserSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'username', 'full_name', 'email', 'role','contact_number')
