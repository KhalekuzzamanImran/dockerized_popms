from decouple import config
import random
import time

import json
from paho.mqtt import client as mqtt_client

broker_address = config('BROKER_ADDRESS')
port = int(config('BROKER_PORT'))
username = config('BROKER_USERNAME')
password = config('BROKER_PASSWORD')

# generate client ID with pub prefix randomly
client_id = f'mqtt-{random.randint(0, 1000)}'


def connect_mqtt():
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

def publish(client):
    data = json.dumps({
            "pm1_0(ug/m3)":80,
            "pm2_5(ug/m3)":12,
            "pm10_0(ug/m3)":12,
            "hum(%)":40,
            "temp_1(*C)":21.39999962,
            "temp_2(*C)":21.22999954,
            "pressure(Pa)":100450.6016,
            "alt(m)":20.91385078,
            "gas(ppm)":393,
            "dp(*C)":7.234584808
        })

    result =  client.publish('incidentPlace/IPX0000001/sensor_data', data)

    if not result[0]:
        print(f"Send `{data}` to incidentPlace/IPX0000001/sensor_data")
    else:
        print(f"Failed to send message to topic incidentPlace/IPX0000001/sensor_data")

    # client.loop_stop()


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()



