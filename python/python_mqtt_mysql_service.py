#!/usr/bin/python3
import MySQLdb
import paho.mqtt.client as mqtt
import ssl
import json 
import os
import sys
import logging

# MQTT Settings
MQTT_Broker = os.getenv('MOSQUITTO_IP')
MQTT_Port = 1883
Keep_Alive_Interval = 60
MQTT_Topic = [("devices/#", 0)]
MQTT_User = os.getenv('MOSQUITTO_USERNAME')
MQTT_Pass = os.getenv('MOSQUITTO_PASSWORD')

# MYSQL Settings
mysqlHost = os.getenv('MYSQL_IP')
mysqlUser = os.getenv('MYSQL_USER')
mysqlPassword = os.getenv('MYSQL_ROOT_PASSWORD')
mysqlDbName = os.getenv('MYSQL_DATABASE')
#print(MQTT_Broker, MQTT_Port, MQTT_User ,MQTT_Pass, mysqlHost, mysqlUser, mysqlPassword, mysqlDbName)

# Subscribe
def on_connect(client, userdata, flags, rc):
    mqttc.subscribe(MQTT_Topic, 0)

def message_to_mysql(db, client ,topic, payload):
    #print("Insert to SQL")
    cursor = db.cursor()
    insertRequest = "INSERT INTO messages(client_id,topic,payload,created_at,deleted_at) VALUES ('%s','%s','%s',NOW(),NULL)" % (client, topic, payload)
    cursor.execute(insertRequest)
    db.commit()

def on_message(mosq, obj, msg):
    decode_payload = str(msg.payload.decode("utf-8","ignore"))
    try:
        json_data = json.loads(decode_payload)
        if "client_id" in json_data:
            db = MySQLdb.connect(host=mysqlHost, user=mysqlUser, password=mysqlPassword, database=mysqlDbName,charset='utf8mb4')
            message_to_mysql(db,json_data["client_id"],msg.topic,decode_payload)
            db.close()
        else:
            db = MySQLdb.connect(host=mysqlHost, user=mysqlUser, password=mysqlPassword, database=mysqlDbName,charset='utf8mb4')
            message_to_mysql(db,"UNKNOWN",msg.topic,decode_payload)
            db.close()
    except ValueError as e:
        print("No JSON ")
        pass

def on_subscribe(mosq, obj, mid, granted_qos):
    pass

mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

mqttc.username_pw_set(MQTT_User, MQTT_Pass)

try:
    mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))
    print("MQTT connection: ON")
except:
    sys.exit("Connection to MQTT Broker failed")
# Continue the network loop & close db-connection
mqttc.loop_forever()
# mariadb_connection.close()
