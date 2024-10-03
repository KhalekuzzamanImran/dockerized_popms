from accounts.mixins import contact_number_validator
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
import uuid


class Role(models.Model):
    id = models.UUIDField(db_column='role_id', primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(db_column='name', max_length=64)
    key = models.CharField(db_column='key', max_length=64)

    def __str__(self):
        return self.key

    class Meta:
        verbose_name_plural = 'Roles'
        db_table = 'role'
         
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users require an email field')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None
    id = models.UUIDField(db_column='user_id', primary_key=True, default=uuid.uuid4, editable=False)
    role = models.ForeignKey('accounts.Role', db_column='role_id', on_delete=models.SET_NULL, null=True, related_name='users',)
    full_name = models.CharField(db_column='full_name', max_length=64)
    password = models.CharField(db_column='password', max_length=256)
    email = models.EmailField(db_column='email', max_length=100, unique=True)
    contact_number = models.CharField(db_column='contact_number', max_length=11, validators=[contact_number_validator])
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'Users'
        db_table = 'user'
        ordering = ['-date_joined']


