from djongo import models as mongoModels
from datetime import datetime
import pytz

def default_time():
    return pytz.utc.localize(datetime.now())

class POPMSA006ExternalInfo(mongoModels.Model):
    _id = mongoModels.ObjectIdField()
    created_time = mongoModels.DateTimeField(default=default_time)
    deviceCode = mongoModels.CharField(max_length=256)
    topic = mongoModels.CharField(max_length=256)
    mainVoltage = mongoModels.FloatField()
    rectifierCurrent = mongoModels.FloatField()
    loadCurrentValue = mongoModels.FloatField()
    loadVoltageValue = mongoModels.FloatField()
    batteryVoltageValue = mongoModels.FloatField()
    batteryCurrentValue = mongoModels.FloatField()
    batteryTemperatureValue = mongoModels.FloatField()
    batteryTimeLeftValue = mongoModels.FloatField()
    batteryRemainingCapacityValue = mongoModels.FloatField()
    batteryUsedCapacityValue = mongoModels.FloatField()
    
    class Meta:
        _use_db = 'nonrel'

    def __str__(self):
        return self.device_code


class TemporaryPOPMSA006ExternalInfo(mongoModels.Model):
    _id = mongoModels.ObjectIdField()
    created_time = mongoModels.DateTimeField(default=default_time)
    deviceCode = mongoModels.CharField(max_length=256)
    topic = mongoModels.CharField(max_length=256)
    mainVoltage = mongoModels.FloatField()
    rectifierCurrent = mongoModels.FloatField()
    loadCurrentValue = mongoModels.FloatField()
    loadVoltageValue = mongoModels.FloatField()
    batteryVoltageValue = mongoModels.FloatField()
    batteryCurrentValue = mongoModels.FloatField()
    batteryTemperatureValue = mongoModels.FloatField()
    batteryTimeLeftValue = mongoModels.FloatField()
    batteryRemainingCapacityValue = mongoModels.FloatField()
    batteryUsedCapacityValue = mongoModels.FloatField()
    
    class Meta:
        _use_db = 'nonrel'

    def __str__(self):
        return self.device_code
    
pytz.utc.localize(datetime.now())
class TodayPOPMSA006ExternalInfo(mongoModels.Model):
    _id = mongoModels.ObjectIdField()
    created_time = mongoModels.DateTimeField(default=default_time)
    deviceCode = mongoModels.CharField(max_length=256)
    topic = mongoModels.CharField(max_length=256)
    mainVoltage = mongoModels.FloatField()
    rectifierCurrent = mongoModels.FloatField()
    loadCurrentValue = mongoModels.FloatField()
    loadVoltageValue = mongoModels.FloatField()
    batteryVoltageValue = mongoModels.FloatField()
    batteryCurrentValue = mongoModels.FloatField()
    batteryTemperatureValue = mongoModels.FloatField()
    batteryTimeLeftValue = mongoModels.FloatField()
    batteryRemainingCapacityValue = mongoModels.FloatField()
    batteryUsedCapacityValue = mongoModels.FloatField()
    
    class Meta:
        _use_db = 'nonrel'

    def __str__(self):
        return self.device_code
    

class Last7DaysPOPMSA006ExternalInfo(mongoModels.Model):
    _id = mongoModels.ObjectIdField()
    created_time = mongoModels.DateTimeField(default=default_time)
    deviceCode = mongoModels.CharField(max_length=256)
    topic = mongoModels.CharField(max_length=256)
    mainVoltage = mongoModels.FloatField()
    rectifierCurrent = mongoModels.FloatField()
    loadCurrentValue = mongoModels.FloatField()
    loadVoltageValue = mongoModels.FloatField()
    batteryVoltageValue = mongoModels.FloatField()
    batteryCurrentValue = mongoModels.FloatField()
    batteryTemperatureValue = mongoModels.FloatField()
    batteryTimeLeftValue = mongoModels.FloatField()
    batteryRemainingCapacityValue = mongoModels.FloatField()
    batteryUsedCapacityValue = mongoModels.FloatField()
    
    class Meta:
        _use_db = 'nonrel'

    def __str__(self):
        return self.device_code
    

class Last30DaysPOPMSA006ExternalInfo(mongoModels.Model):
    _id = mongoModels.ObjectIdField()
    created_time = mongoModels.DateTimeField(default=default_time)
    deviceCode = mongoModels.CharField(max_length=256)
    topic = mongoModels.CharField(max_length=256)
    mainVoltage = mongoModels.FloatField()
    rectifierCurrent = mongoModels.FloatField()
    loadCurrentValue = mongoModels.FloatField()
    loadVoltageValue = mongoModels.FloatField()
    batteryVoltageValue = mongoModels.FloatField()
    batteryCurrentValue = mongoModels.FloatField()
    batteryTemperatureValue = mongoModels.FloatField()
    batteryTimeLeftValue = mongoModels.FloatField()
    batteryRemainingCapacityValue = mongoModels.FloatField()
    batteryUsedCapacityValue = mongoModels.FloatField()
    
    class Meta:
        _use_db = 'nonrel'

    def __str__(self):
        return self.device_code
    

class ThisYearPOPMSA006ExternalInfo(mongoModels.Model):
    _id = mongoModels.ObjectIdField()
    created_time = mongoModels.DateTimeField(default=default_time)
    deviceCode = mongoModels.CharField(max_length=256)
    topic = mongoModels.CharField(max_length=256)
    mainVoltage = mongoModels.FloatField()
    rectifierCurrent = mongoModels.FloatField()
    loadCurrentValue = mongoModels.FloatField()
    loadVoltageValue = mongoModels.FloatField()
    batteryVoltageValue = mongoModels.FloatField()
    batteryCurrentValue = mongoModels.FloatField()
    batteryTemperatureValue = mongoModels.FloatField()
    batteryTimeLeftValue = mongoModels.FloatField()
    batteryRemainingCapacityValue = mongoModels.FloatField()
    batteryUsedCapacityValue = mongoModels.FloatField()
    
    class Meta:
        _use_db = 'nonrel'

    def __str__(self):
        return self.device_code
    

    


    
