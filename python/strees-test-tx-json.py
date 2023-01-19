#! c:\python34\python3
#!/usr/bin/env python
##demo code provided by Steve Cope at www.steves-internet-guide.com
##email steve@steves-internet-guide.com
##Free to use for any purpose
##If you like and use this code you can
##buy me a drink here https://www.paypal.me/StepenCope
import signal
import time
import json
import paho.mqtt.client as paho
##edit these settings
broker="192.168.10.11"
port=1883
blocks=50 #edit for number of blocks
messages=200 #edit for messages per block
message_size=1000 #edit for size of message
M_delay=0.00001 #delay between messages
Loop_delay=2
json_data = {}
inject_error=False
error_block=3 #put error in this block
pub_topic="v3/test"
#inject_error=True
### end edit
#broker="test.mosquitto.org"
#define callback
def on_message(client, userdata, message):
   print(str(message.payload.decode("utf-8")))

def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
        client.subscribe("tests/results")
    else:
        print("Bad connection Returned code=",rc)


cname="tx-client-"+str(int(time.time()))
client= paho.Client(cname)
#assign function to callback          
######
client.connected_flag=False
client.on_message=on_message
client.on_connect=on_connect
client.username_pw_set("mosquitto", "vedroid")
#####
print("connecting to broker ",broker)
client.connect(broker,port)#connect
client.loop_start()
while not client.connected_flag:
   time.sleep(.1)
print("subscribing ")
client.subscribe("test/results")#subscribe
print("publishing ")
count=1
message_rate=0
loop_count=0

while loop_count<blocks:
   stime=time.time()
   for count in range(1,messages+1):
      client.loop(.0001)
      c=str(count).rjust(6,"0")
      l=str(loop_count).rjust(6,"0")
      json_data["client_id"] = c
      json_data["other"] = l
      message=json.dumps(json_data, indent = 4)
      if loop_count==4 and inject_error:
         if count==error_block:
            print ("publishing error ")
            continue
      client.publish(pub_topic,message)#publish
      time.sleep(M_delay)
      message=""
   time_taken=time.time()-stime
   print("Time taken = %.3f " %time_taken)
   message_rate=messages/time_taken
   print("message rate %.3f " %message_rate," messages per second")
   message_rate=messages*message_size/time_taken
   print("message rate %.3f" %message_rate," Bytes per second")

   time.sleep(Loop_delay)
   count=0
   loop_count+=1
   
time.sleep(20)
client.disconnect() #disconnect
client.loop_stop() #stop loop
