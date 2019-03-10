import paho.mqtt.client as mqtt
import time

############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
########################################
broker_address="127.0.0.1"
print("creating new instance")
client = mqtt.Client("P1") #create new instance
client.username_pw_set("temp1","ascp01")
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
print("Subscribing to topic","QQ010/G0/bedroom/temp1/get")
client.subscribe("QQ010/G0/bedroom/temp1/get")
print("Subscribing to topic","QQ010/G0/bedroom/switch1/set")
client.subscribe("QQ010/G0/bedroom/switch1/set")
time.sleep(4) # wait
client.loop_stop() #stop the loop
