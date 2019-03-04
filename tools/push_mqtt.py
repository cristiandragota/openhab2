import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
    if message.topic == QQ010/G0/bedroom/temp1/set:
        set_temp1 = str(message.payload.decode("utf-8"))
            print("message received, the set value is:  " ,set_temp1)
    if message.topic == QQ010/G0/bedroom/switch1/set:
        set_switch1 = str(message.payload.decode("utf-8"))
            print("message received, the unit is: " ,set_temp1)

mqttpush = mqtt.Client("Push_mqtt_client")
mqttpush.username_pw_set("temp1","ascp01")
mqttpush.on_message = on_message
#mqttpush.on_connect = on_connect
#mqttpush.on_publish = on_publish
#mqttpush.on_subscribe = on_subscribe

Broker = "futureconcepts.tech"

print("connecting to broker")
mqttpush.connect(Broker, 1883, 60)
mqttpush.loop_start()
print("Subscribing to topic: ","QQ010/G0/bedroom/temp1/set")
mqttpush.subscribe("QQ010/G0/bedroom/temp1/set")
mqttpush.subscribe("QQ010/G0/bedroom/switch1/set")
print("Publish to topic: ","QQ010/G0/bedroom/temp1/get")
mqttpush.publish("QQ010/G0/bedroom/temp1/get","22.3")
time.sleep(60)
#mqttpush.loop_stop()
