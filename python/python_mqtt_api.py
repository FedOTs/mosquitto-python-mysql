#!/usr/bin/python3

from flask import Flask
from flask import request

import paho.mqtt.client as mqtt
import ssl
import os
import json 

# MQTT Settings
MQTT_Broker = os.getenv('MOSQUITTO_IP')
MQTT_Port = 1883
Keep_Alive_Interval = 60
MQTT_Topic = [("#", 0)]
MQTT_User = os.getenv('MOSQUITTO_USERNAME')
MQTT_Pass = os.getenv('MOSQUITTO_PASSWORD')
TOKEN = os.getenv('API_TOKEN')

app = Flask(__name__)

@app.route("/publish/"+TOKEN+"/", methods=["POST"])
def publish():
    post_param = ['user_id', 'client_id', 'topic','payload']
    
    dict_data = request.form
    
    for param in post_param:
        if param not in dict_data.keys():
            return "error: Нет обязательного параметра {0}".format(param)

    user_id = dict_data["user_id"]
    client_id = dict_data["client_id"]
    topic = dict_data["topic"]
    payload = dict_data["payload"]
    mqttc = mqtt.Client(client_id)

    mqttc.on_publish = on_publish

    mqttc.username_pw_set("mosquitto", "vedroid")
    mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))
    ret = mqttc.publish(topic, payload)
    return "<p>Hello, World!</p>"

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass