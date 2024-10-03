from django.contrib.auth import get_user_model
from accounts.models import CustomUser
from django.db import models

User = get_user_model()


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_column='created_at', auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(db_column='updated_at', auto_now=True, editable=False)
    created_by = models.ForeignKey(CustomUser, db_column='created_by', on_delete=models.SET_NULL, null=True, related_name="%(app_label)s_%(class)s_created_by")
    updated_by = models.ForeignKey(CustomUser, db_column='updated_by', on_delete=models.SET_NULL, null=True, related_name="%(app_label)s_%(class)s_modified_by")
    is_active = models.BooleanField(db_column='is_active', default=True)

    class Meta:
        abstract = True
