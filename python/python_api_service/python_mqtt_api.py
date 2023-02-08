#!/usr/bin/python3

from flask import Flask
from flask import request
from flask_cors import CORS

import paho.mqtt.client as mqtt
import ssl
import os
import json 
import logging

#logging config
logging.basicConfig(filename='python_mqtt_api.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s', level=logging.ERROR)

# MQTT Settings
MQTT_Broker = os.getenv('MOSQUITTO_IP')
MQTT_Port = 1883
Keep_Alive_Interval = 60
MQTT_User = os.getenv('MOSQUITTO_USERNAME')
MQTT_Pass = os.getenv('MOSQUITTO_PASSWORD')
TOKEN = os.getenv('API_TOKEN')

app = Flask(__name__)
CORS(app)

@app.route("/publish", methods=["POST"])
def publish():
    post_param = ['user_id', 'client_id','payload','payload_changes']
    
    dict_data = request.json
    #logging.error("Входящие данные %s", dict_data.items())

    for param in post_param:
        if param not in dict_data.keys():
            logging.error("error: Нет обязательного параметра %s", param)
            return "error: Нет обязательного параметра {0}".format(param)

    user_id = dict_data["user_id"]
    client_id = dict_data["client_id"]
    topic = "devices/set/{0}".format(client_id)
    payload = dict_data["payload"]
    payload_changes = dict_data["payload_changes"]

    try:
        data = jsonCompare(payload, payload_changes)
    except:
        logging.error("%s json compare data error", [payload, payload_changes])

    mqttc = mqtt.Client(client_id)

    mqttc.on_publish = on_publish

    mqttc.username_pw_set("mosquitto", "vedroid")
    mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))
    ret = mqttc.publish(topic, str(data))
    return "<p>Hello, World!</p>"

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass

def jsonCompare(payload, changes):
    data = {}
    i2clst = []
    rs485lst = []
    for keyheader, valueheader in changes.items():
        if keyheader in ["relays","analog_ports"]:
            for key_, _ in payload.items():
                if keyheader == key_:
                    for key, value in valueheader.items():
                        data[keyheader] = {key: value}
        elif keyheader == "i2c":
            for ob in valueheader:
                for ob_ in payload[keyheader]:
                    if ob["adres"] == ob_["adres"]:
                        i2clst.append(ob)
        elif keyheader == "rs485":
            for ob in valueheader:
                for ob_ in payload[keyheader]:
                    if ob["id"] == ob_["id"]:
                        rs485lst.append(ob)
    if len(i2clst) > 0:
        data["i2c"] = i2clst
    if len(rs485lst) > 0:
        data["rs485"] = i2clst

    return data