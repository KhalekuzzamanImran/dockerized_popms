import django
import os

from celery.schedules import crontab
from celery import Celery

from datetime import timedelta, datetime
from django.conf import settings
import json
import logging

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'popms.settings')

logger = logging.getLogger(__name__)

app = Celery('popms')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

def prepare_popmsa006_data(data):
    import numpy as np

    items = {
        "ac_temp_1" : 0,
        "ac_temp_2" : 0,
        "env_temp_1" : 0,
        "env_hum_1" : 0,
        "env_dp_1" : 0,
        "env_temp_2" : 0,
        "env_hum_2" : 0,
        "env_dp_2" : 0,
        "door_state_1" : 0,
        "door_state_2" : 0,
        "smoke_state" : 0,
        "ua" : 0,
        "ub" : 0,
        "uc" : 0,
        "avln" : 0,
        "uab" : 0,
        "ubc" : 0,
        "uca" : 0,
        "avll" : 0,
        "ia" : 0,
        "ib" : 0,
        "ic" : 0,
        "avc" : 0,
        "pa" : 0,
        "pb" : 0,
        "pc" : 0,
        "sa" : 0,
        "sb" : 0,
        "sc" : 0,
        "qa" : 0,
        "qb" : 0,
        "qc" : 0,
        "totkw" : 0,
        "totkva" : 0,
        "totkvar" : 0,
        "pfa" : 0,
        "pfb" : 0,
        "pfc" : 0,
        "avpf" : 0,
        "f" : 0,
        "totnkwh" : 0,
        "totnkvah" : 0,
        "totnkvarh" : 0,
    }
    statictics = {}
    for key in items.keys():
        values = [dic.get(key) for dic in data if dic.get(key, None) is not None]
        statictics[key] = np.mean(values) if values else None
    
    data_length = len(data)
    statictics['timestamp'] = data[data_length - 1]['timestamp'] if data_length > 0 else None

    return statictics


def prepare_popmsa006_external_info(data):
    import numpy as np

    items = {
        "mainVoltage": 0,
        "rectifierCurrent": 0,
        "loadCurrentValue": 0,
        "loadVoltageValue": 0,
        "batteryVoltageValue": 0,
        "batteryCurrentValue": 0,
        "batteryTemperatureValue": 0,
        "batteryTimeLeftValue": 0,
        "batteryRemainingCapacityValue": 0,
        "batteryUsedCapacityValue": 0
    }

    statictics = {}
    for key in items.keys():
        values = [dic.get(key) for dic in data if dic.get(key) is not None]
        statictics[key] = np.mean(values) if values else None

    return statictics



@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    
    # Datewise POPMSA006 Mongo Create..
    sender.add_periodic_task(
        crontab(minute='*/10'),
        create_last7days_popmsa006_data.s('all_rang'),
    )

    sender.add_periodic_task(
        crontab(minute='*/30'),
        create_last30days_popmsa006_data.s('all_rang'),
    )

    sender.add_periodic_task(
        crontab(minute=0, hour='*/6'),
        create_this_year_popmsa006_data.s('all_rang'),
    )

    sender.add_periodic_task(
        crontab(minute=0, hour=0),
        delete_today_popmsa006_data.s(),
    )

    sender.add_periodic_task(
        crontab(minute=0, hour=0),
        delete_data_older_than_7days_or_30days.s(),
    )

    # sender.add_periodic_task(
    #     crontab(minute=0, hour=0, day_of_week='1'),
    #     delete_last_week_cpm_rt_data.s('all_rang'),
    # )

    # sender.add_periodic_task(
    #     crontab(minute=0, hour=0, day_of_month='1'),
    #     delete_last_month_cpm_rt_data.s('all_rang'),
    # )


    


@app.task
def create_last7days_popmsa006_data(arg):
    from pops.POPMSA006_mongo_models import TemporaryPOPMSA006
    from pops.api.serializers import TemporaryPOPMSA006Serializer, TemporaryPOPMSA006ExternalInfoSerializer

    from pops.temporary_popmsa006_models import TemporaryPOPMSA006ExternalInfo
    from pops.temporary_popmsa006_mixins import date_wise_popmsa006_external_info_create

    from pops.models import Pop, PopDevice, PopDeviceState
    from pops.POPMSA006_mongo_mixins import date_wise_popmsa006_create

    for pop in Pop.objects.filter(is_active=True):
        for device in PopDevice.objects.filter(pop_name=pop.id):
            for state in PopDeviceState.objects.filter(device_code=device.id):
                if str(state.device_code) == 'POPMSA006' and state.date == 'TODAY':
                    if state.topic == 'POPMS/CelestialHubPoP/status':
                        temp_popmsa006_mongo_queryset = TemporaryPOPMSA006.objects.all()
                        data = TemporaryPOPMSA006Serializer(temp_popmsa006_mongo_queryset, many=True).data                 
                        date_wise_popmsa006_create(prepare_popmsa006_data(data), state.device_code, state.topic, ['LAST_7_DAYS'])
                        temp_popmsa006_mongo_queryset.delete()
                        logger.warning(f"TemporaryPOPMSA006 {state.topic} data deleted succesfully")
                    
                    if state.topic == 'temporary/POPMS/CelestialHubPoP/status':
                        temp_popmsa006_mongo_queryset = TemporaryPOPMSA006ExternalInfo.objects.all()
                        data =TemporaryPOPMSA006ExternalInfoSerializer(temp_popmsa006_mongo_queryset, many=True).data
                        date_wise_popmsa006_external_info_create(prepare_popmsa006_external_info(data), state.device_code, state.topic, ['LAST_7_DAYS'])


   


@app.task
def create_last30days_popmsa006_data(arg):
    from pops.POPMSA006_mongo_models import Last7DaysPOPMSA006
    from pops.temporary_popmsa006_models import Last7DaysPOPMSA006ExternalInfo
    from pops.api.serializers import Last7DaysPOPMSA006Serializer, Last7DaysPOPMSA006ExternalInfoSerializer
    from pops.models import Pop, PopDevice, PopDeviceState
    from pops.POPMSA006_mongo_mixins import date_wise_popmsa006_create
    from pops.temporary_popmsa006_mixins import date_wise_popmsa006_external_info_create

    for pop in Pop.objects.filter(is_active=True):
        for device in PopDevice.objects.filter(pop_name=pop.id):
            for state in PopDeviceState.objects.filter(device_code=device.id):
                if str(state.device_code) == 'POPMSA006' and state.date == 'LAST_7_DAYS':
                    if state.topic == 'POPMS/CelestialHubPoP/status':
                        last7days_popmsa006_mongo_queryset = Last7DaysPOPMSA006.objects.order_by('-created_time')[:3]
                        data = Last7DaysPOPMSA006Serializer(last7days_popmsa006_mongo_queryset, many=True).data
                        date_wise_popmsa006_create(prepare_popmsa006_data(data), state.device_code, state.topic, ['LAST_30_DAYS'])
                        # today_popmsa006_mongo_queryset.delete()
                        # logger.warning(f"TodayPOPMSA006 {state.topic} data deleted succesfully")

                    if state.topic == 'temporary/POPMS/CelestialHubPoP/status':
                        last7days_popmsa006_externalInfo_mongo_queryset = Last7DaysPOPMSA006ExternalInfo.objects.order_by('-created_time')[:3]
                        data = Last7DaysPOPMSA006ExternalInfoSerializer(last7days_popmsa006_externalInfo_mongo_queryset, many=True).data
                        date_wise_popmsa006_external_info_create(prepare_popmsa006_external_info(data), state.device_code, state.topic, ['LAST_30_DAYS'])



@app.task
def create_this_year_popmsa006_data(arg):
    from pops.POPMSA006_mongo_models import Last30DaysPOPMSA006
    from pops.temporary_popmsa006_models import Last30DaysPOPMSA006ExternalInfo
    from pops.api.serializers import Last30DaysPOPMSA006Serializer, Last30DaysPOPMSA006ExternalInfoSerializer
    from pops.models import Pop, PopDevice, PopDeviceState
    from pops.POPMSA006_mongo_mixins import date_wise_popmsa006_create
    from pops.temporary_popmsa006_mixins import date_wise_popmsa006_external_info_create

    for pop in Pop.objects.filter(is_active=True):
        for device in PopDevice.objects.filter(pop_name=pop.id):
            for state in PopDeviceState.objects.filter(device_code=device.id):
                if str(state.device_code) == 'POPMSA006' and state.date == 'THIS_YEAR':
                    if state.topic == 'POPMS/CelestialHubPoP/status':
                        last30days_popmsa006_mongo_queryset = Last30DaysPOPMSA006.objects.order_by('-created_time')[:12]
                        data = Last30DaysPOPMSA006Serializer(last30days_popmsa006_mongo_queryset, many=True).data
                        date_wise_popmsa006_create(prepare_popmsa006_data(data), state.device_code, state.topic, ['THIS_YEAR'])
                        # today_popmsa006_mongo_queryset.delete()
                        # logger.warning(f"TodayPOPMSA006 {state.topic} data deleted succesfully")
                    
                    if state.topic == 'temporary/POPMS/CelestialHubPoP/status':
                        last30days_popmsa006_externalInfo_mongo_queryset = Last30DaysPOPMSA006ExternalInfo.objects.order_by('-created_time')[:12]
                        data = Last30DaysPOPMSA006ExternalInfoSerializer(last30days_popmsa006_externalInfo_mongo_queryset, many=True).data
                        date_wise_popmsa006_external_info_create(prepare_popmsa006_external_info(data), state.device_code, state.topic, ['THIS_YEAR'])
                        # today_popmsa006_mongo_queryset.delete()
                        # logger.warning(f"TodayPOPMSA006 {state.topic} data deleted succesfully")


@app.task
def delete_today_popmsa006_data():
    from pops.POPMSA006_mongo_models import TodayPOPMSA006
    from pops.models import Pop, PopDevice, PopDeviceState

    for pop in Pop.objects.filter(is_active=True):
        for device in PopDevice.objects.filter(pop_name=pop.id):
            for state in PopDeviceState.objects.filter(device_code=device.id):
                if (state.date == 'TODAY'):
                    today_popmsa006_queryset = TodayPOPMSA006.objects.all()
                    today_popmsa006_queryset.delete()
                    logger.warning(f"TodayPOPMSA006 {state.topic} data deleted succesfully")


@app.task
def delete_data_older_than_7days_or_30days():
    from pops.models import Pop, PopDevice, PopDeviceState
    from pops.POPMSA006_mongo_models import Last7DaysPOPMSA006, Last30DaysPOPMSA006

    for pop in Pop.objects.filter(is_active=True):
        for device in PopDevice.objects.filter(pop_name=pop.id):
            for state in PopDeviceState.objects.filter(device_code=device.id):
                if (state.date == 'LAST_7_DAYS'):
                    end_time = datetime.now() - timedelta(days=6)
                    records = Last7DaysPOPMSA006.objects.filter(created_time__lt=(end_time))
                    records.delete()
                    logger.warning(f"----------------------Last7DaysPOPMSA006 data deleted succesfully-----------------------")

                if (state.date == 'LAST_30_DAYS'):
                    end_time = datetime.now() - timedelta(days=29)
                    records = Last30DaysPOPMSA006.objects.filter(created_time__lt=(end_time))
                    records.delete()
                    logger.warning(f"----------------------Last30DaysPOPMSA006 data deleted succesfully-----------------------")

                    





