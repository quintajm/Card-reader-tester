import paho.mqtt.client as mqtt
import subprocess
import os

#def publishMsg(topic="TestFinished" ,message ='BT_test_Activated'):
#    client = mqtt.client()
#    client.publish(topic, f"{message}")
#    client.disconect()

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("BT_test")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    #If message forward move forward
    if msg.payload == b"forward":
        print("brrr...forward")
        os.system("python3 CONTROL_forward.py")
        #publishMsg()
    # If message backward move backward
    if msg.payload == b"backward":
        print('brrr...backwards')
        os.system("python3 CONTROL_backward.py")
        #publishMsg()
    # If message stop
    if msg.payload == b"stop":
        print('brrr...stop')
        os.system("python3 CONTROL_stop.py")
        #publishMsg()


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("10.0.0.211",1883,60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
