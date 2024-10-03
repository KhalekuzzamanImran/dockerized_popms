from base.models import BaseModel
from django.db import models
import uuid

class Pop(BaseModel):
    choices_type = (
        ('CRITICAL', 'Critical'),
        ('MAJOR', 'Major'),
        ('MINOR', 'Minor')
    )

    network_choice_type = (
        ('ONLINE', 'On Line'),
        ('OFFLINE', 'Off Line'),
        ('WARNING', 'Warning')
    )

    id = models.UUIDField(db_column='pop_id', primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=64, db_column='status', choices=choices_type)
    code = models.CharField(db_column='code', unique=True, max_length=200)
    name = models.CharField(db_column='name', max_length=360)
    address = models.TextField(db_column='address', max_length=360)
    latitude = models.FloatField(db_column='latitude')
    longitude = models.FloatField(db_column='longitude')
    network_status = models.CharField(max_length=12, db_column='network_status', choices=network_choice_type)
    user = models.ForeignKey('accounts.CustomUser', db_column='user_id', on_delete=models.CASCADE, related_name='user_pops')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Pops'
        db_table = 'pop'
        ordering = ['-created_at']


class PopDevice(BaseModel):
    choices_type = (
        ('CRITICAL', 'Critical'),
        ('MAJOR', 'Major'),
        ('MINOR', 'Minor')
    )

    id = models.UUIDField(db_column='pop_device_id',default=uuid.uuid4, editable=False, primary_key=True)
    pop_name = models.ForeignKey('Pop', db_column='pop_name', on_delete=models.CASCADE)
    status = models.CharField(max_length=64, db_column='status', choices=choices_type)
    code = models.CharField(db_column='code', unique=True, max_length=200)
    name = models.CharField(db_column='name', max_length=360)
    remark = models.TextField(db_column='remark', max_length=360, null=True, blank=True)
    phy_details = models.JSONField(db_column='phy_details', null=True, blank=True)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name_plural = 'Pop Devices'
        db_table = 'popdevice'
        ordering = ['-created_at']

        indexes = [
            models.Index(fields=['code']),
            models.Index(fields=['status']),
            models.Index(fields=['is_active']),
            models.Index(fields=['created_at']),
        ]


class PopDeviceState(BaseModel):
    choices_type = (
        ('TODAY', 'Today'),
        ('LAST_7_DAYS', 'Last 7 days'),
        ('LAST_30_DAYS', 'Last 30 days'),
        ('THIS_YEAR', 'This Year'),
    )

    id = models.UUIDField(db_column='incident_id', primary_key=True, default=uuid.uuid4, editable=False)
    device_code = models.ForeignKey(PopDevice, db_column='device_code', on_delete=models.CASCADE)
    topic = models.CharField(db_column='topic', max_length=256)
    date = models.CharField(max_length=256, db_column='date', choices=choices_type)
    data = models.JSONField(db_column='data')

    def __str__(self):
        return f'{self.device_code}'

    class Meta:
        verbose_name_plural = 'Pop Device States'
        db_table = 'pop_device_state'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['created_at']),
            models.Index(fields=['is_active'])
        ]

