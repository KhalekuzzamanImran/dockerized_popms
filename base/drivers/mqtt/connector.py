import paho.mqtt.client as mqtt
from decouple import config
import time


class MQTT(object):
    def __init__(self) -> None:
        """
            On initialization of the connection class with MQTT,
        environment settings are loaded at runtime,
        and served under the context of the instance.
        """

        self.connected = False
        self.broker_address = config('BROKER_ADDRESS')
        self.port = int(config('BROKER_PORT'))
        self.username = config('BROKER_USERNAME')
        self.password = config('BROKER_PASSWORD')

    def on_connect(self, client, usedata, flags, rc):
        if rc==0:
            print('Client is connected !')
            self.connected = True
        else:
            print('Connection failed')

    def client(self):
        """
            Create a connection to MQTT
        Raises:
            error: Exception
        Returns:
            Coroutine[Any, Any, ConnectionType@connect]
        """
        try:
            client = mqtt.Client('MQTT_popms')
            client.username_pw_set(self.username, password=self.password)
            client.on_connect=self.on_connect
            client.connect(self.broker_address, port=self.port)
            client.loop_start()

            while not self.connected:
                time.sleep(0.2)

            return client

        except Exception as error:
            raise error
