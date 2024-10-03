
import django
import os
import sys
import time 


count = 0
rt_data = []
eny_data = []
temp = []

current2 = os.path.dirname(os.path.realpath(__file__))
current1 = os.path.dirname(current2)
parent = os.path.dirname(current1)
sys.path.append(parent)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'popms.settings')
django.setup()

from pops.models import PopDevice, PopDeviceState
from pops.POPMSA006_mongo_mixins import popmsa006_mongo_create
from pops.temporary_popmsa006_mixins import popmsA006ExternalInfo_mongo_create

from paho.mqtt import client as mqtt_client
# from devices.models import Device
# from devices.air_quality_mixins import air_quality_mongo_create
# from devices.thermohygrometer_modhumati_mixins import thermohygrometer_mongo_create
from decouple import config
import random
import json



broker_address = config('BROKER_ADDRESS')
port = int(config('BROKER_PORT'))
username = config('BROKER_USERNAME')
password = config('BROKER_PASSWORD')

# generate client ID with pub prefix randomly
client_id = f'mqtt-{random.randint(0, 100)}'

# MQRTT_RT_DATA normalize or remove redundency

def remove_unnecessary_data(data):
    temp = data.copy()

    if (temp['dataFlow'] == 1):
        del temp['dataFlow']
        return temp

    if (temp['dataFlow'] == 0):
        del temp['dev_ID']
        del temp['dataFlow']
        del temp['timestamp']
        return temp


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker_address, port)
    return client


def subscribe(client: mqtt_client):
    
    def on_message(client, userdata, msg):
        global count
        global rt_data, eny_data, temp
        # print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

        try:
            data = msg.payload.decode()  # json formated data
            data = json.loads(data)      # python dictionary
            
            # POP Devices
            if (msg.topic == 'POPMS/CelestialHubPoP/status'):
                temp.append(remove_unnecessary_data(data))

                if (data['dataFlow'] == 1):
                    count = 0
                    # print(temp)
                    popmsa006_mongo_create(temp, msg.topic)
                    temp = []

            # TemporaryPOPMS External Info
            elif (msg.topic == 'temporary/POPMS/CelestialHubPoP/status'):
                popmsA006ExternalInfo_mongo_create(data, msg.topic)
                

        except Exception as error:
            raise error

    # for device in Device.objects.filter(is_active=True):
    #     client.subscribe(device.code)
        # print('===========================================================================', device.code)

    # client.subscribe('MQTT_RT_DATA')
        
    for pop_device in PopDevice.objects.filter(is_active=True):
        for state in PopDeviceState.objects.filter(device_code=pop_device.id):
            if state.date == 'TODAY':   
                client.subscribe(state.topic)
            # print('===========================================================================', state.topic)

    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
    
