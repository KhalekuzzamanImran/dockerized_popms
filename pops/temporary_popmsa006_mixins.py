from pops.temporary_popmsa006_models import POPMSA006ExternalInfo, TodayPOPMSA006ExternalInfo, TemporaryPOPMSA006ExternalInfo, Last7DaysPOPMSA006ExternalInfo, Last30DaysPOPMSA006ExternalInfo, ThisYearPOPMSA006ExternalInfo

import logging
logger = logging.getLogger(__name__)

def popmsA006ExternalInfo_mongo_create(data, topic):

    popmsA006ExternalInfo = POPMSA006ExternalInfo.objects.create(
        deviceCode = 'POPMSA006',
        topic = topic,
        mainVoltage = data.get('mains voltage', None),
        rectifierCurrent = data.get('rectifier current', None),
        loadCurrentValue = data.get('loadCurrentValue', None),
        loadVoltageValue = data.get('loadVoltageValue', None),
        batteryVoltageValue = data.get('batteryVoltageValue', None),
        batteryCurrentValue = data.get('batteryCurrentsValue', None),
        batteryTemperatureValue = data.get('batteryTemperaturesValue', None),
        batteryTimeLeftValue = data.get('batteryTimeLeftValue', None),
        batteryRemainingCapacityValue = data.get('batteryRemainingCapacityValue', None),
        batteryUsedCapacityValue = data.get('batteryUsedCapacityValue', None),
    )

    logger.info(f"mongo_db = POPMSA006ExternalInfo, topic = {topic} created {popmsA006ExternalInfo._id} succesfully")
    print('<!---------------------------Data successfully inserted in POPMSA006ExternalInfo------------------------------!>')


    todayPOPMSA006ExternalInfo = TodayPOPMSA006ExternalInfo.objects.create(
        deviceCode = 'POPMSA006',
        topic = topic,
        mainVoltage = data.get('mains voltage', None),
        rectifierCurrent = data.get('rectifier current', None),
        loadCurrentValue = data.get('loadCurrentValue', None),
        loadVoltageValue = data.get('loadVoltageValue', None),
        batteryVoltageValue = data.get('batteryVoltageValue', None),
        batteryCurrentValue = data.get('batteryCurrentsValue', None),
        batteryTemperatureValue = data.get('batteryTemperaturesValue', None),
        batteryTimeLeftValue = data.get('batteryTimeLeftValue', None),
        batteryRemainingCapacityValue = data.get('batteryRemainingCapacityValue', None),
        batteryUsedCapacityValue = data.get('batteryUsedCapacityValue', None),
    )

    logger.info(f"mongo_db = TodayPOPMSA006ExternalInfo, topic = {topic} created {todayPOPMSA006ExternalInfo._id} succesfully")
    print('<!---------------------------Data successfully inserted in TodayPOPMSA006ExternalInfo------------------------------!>')


    temporaryPOPMSA006ExternalInfo = TemporaryPOPMSA006ExternalInfo.objects.create(
        deviceCode = 'POPMSA006',
        topic = topic,
        mainVoltage = data.get('mains voltage', None),
        rectifierCurrent = data.get('rectifier current', None),
        loadCurrentValue = data.get('loadCurrentValue', None),
        loadVoltageValue = data.get('loadVoltageValue', None),
        batteryVoltageValue = data.get('batteryVoltageValue', None),
        batteryCurrentValue = data.get('batteryCurrentsValue', None),
        batteryTemperatureValue = data.get('batteryTemperaturesValue', None),
        batteryTimeLeftValue = data.get('batteryTimeLeftValue', None),
        batteryRemainingCapacityValue = data.get('batteryRemainingCapacityValue', None),
        batteryUsedCapacityValue = data.get('batteryUsedCapacityValue', None),
    )

    logger.info(f"mongo_db = TemporaryPOPMSA006ExternalInfo, topic = {topic} created {temporaryPOPMSA006ExternalInfo._id} succesfully")
    print('<!---------------------------Data successfully inserted in TemporaryPOPMSExternalInfo------------------------------!>')


def date_wise_popmsa006_external_info_create(data, device_code, topic, flag):
    # print(data, topic)

    if 'LAST_7_DAYS' in flag:
        last7days_popmsa006_external_info = Last7DaysPOPMSA006ExternalInfo.objects.create(
            deviceCode = device_code,
            topic = topic,
            mainVoltage = data.get('mainVoltage', None),
            rectifierCurrent = data.get('rectifierCurrent', None),
            loadCurrentValue = data.get('loadCurrentValue', None),
            loadVoltageValue = data.get('loadVoltageValue', None),
            batteryVoltageValue = data.get('batteryVoltageValue', None),
            batteryCurrentValue = data.get('batteryCurrentValue', None),
            batteryTemperatureValue = data.get('batteryTemperatureValue', None),
            batteryTimeLeftValue = data.get('batteryTimeLeftValue', None),
            batteryRemainingCapacityValue = data.get('batteryRemainingCapacityValue', None),
            batteryUsedCapacityValue = data.get('batteryUsedCapacityValue', None), 
        )

        logger.info(f"mongo_db = Last7DaysPOPMSA006ExternalInfo, topic = {topic} created {last7days_popmsa006_external_info._id} succesfully")
        print('<!---------------------------Data successfully inserted in Last7DaysPOPMSA006ExternalInfo------------------------------!>')

    if 'LAST_30_DAYS' in flag:
        last30days_popmsa006_external_info = Last30DaysPOPMSA006ExternalInfo.objects.create(
            deviceCode = device_code,
            topic = topic,
            mainVoltage = data.get('mainVoltage', None),
            rectifierCurrent = data.get('rectifierCurrent', None),
            loadCurrentValue = data.get('loadCurrentValue', None),
            loadVoltageValue = data.get('loadVoltageValue', None),
            batteryVoltageValue = data.get('batteryVoltageValue', None),
            batteryCurrentValue = data.get('batteryCurrentValue', None),
            batteryTemperatureValue = data.get('batteryTemperatureValue', None),
            batteryTimeLeftValue = data.get('batteryTimeLeftValue', None),
            batteryRemainingCapacityValue = data.get('batteryRemainingCapacityValue', None),
            batteryUsedCapacityValue = data.get('batteryUsedCapacityValue', None), 
        )

        logger.info(f"mongo_db = Last30DaysPOPMSA006ExternalInfo, topic = {topic} created {last30days_popmsa006_external_info._id} succesfully")
        print('<!---------------------------Data successfully inserted in Last30DaysPOPMSA006ExternalInfo------------------------------!>') 

    if 'THIS_YEAR' in flag:
        thisyear_popmsa006_external_info = ThisYearPOPMSA006ExternalInfo.objects.create(
            deviceCode = device_code,
            topic = topic,
            mainVoltage = data.get('mainVoltage', None),
            rectifierCurrent = data.get('rectifierCurrent', None),
            loadCurrentValue = data.get('loadCurrentValue', None),
            loadVoltageValue = data.get('loadVoltageValue', None),
            batteryVoltageValue = data.get('batteryVoltageValue', None),
            batteryCurrentValue = data.get('batteryCurrentValue', None),
            batteryTemperatureValue = data.get('batteryTemperatureValue', None),
            batteryTimeLeftValue = data.get('batteryTimeLeftValue', None),
            batteryRemainingCapacityValue = data.get('batteryRemainingCapacityValue', None),
            batteryUsedCapacityValue = data.get('batteryUsedCapacityValue', None), 
        )

        logger.info(f"mongo_db = ThisYearPOPMSA006ExternalInfo, topic = {topic} created {thisyear_popmsa006_external_info._id} succesfully")
        print('<!---------------------------Data successfully inserted in ThisYearPOPMSA006ExternalInfo------------------------------!>')

    