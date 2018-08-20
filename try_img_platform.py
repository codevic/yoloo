# some_file.py
import sys
import numpy as np
# sys.path.insert(0, '/Users/Codeo/yolo_test_MQTT/darkflow/ClearBlade-Python-SDK')
sys.path.insert(0, '/Users/Codeo/yolo_test_MQTT/darkflow/clearblade')
from clearblade.ClearBladeCore import System, Query, Developer, Users
from darkflow.net.build import TFNet
import cv2
import PIL
import scipy
import _pickle as cpickle
import time
from struct import *


url = "http://localhost:3000"

# mySystem = System(SystemKey, SystemSecret, url, safe=False)

SystemKey = "d4a68fb60becb78bcdb4ecdffd2c"
SystemSecret = "D4A68FB60BD2DF8998A5EBC0E5EA01"

mySystem = System(SystemKey, SystemSecret, safe = False)


sanket = mySystem.User("vsoni@clearblade.com", "ashokverma")
print("\n HI\n")
# Use Sanket to access a messaging client
mqtt = mySystem.Messaging(sanket)

imgcv = cv2.imread("./sample_img/sample_dog.jpg")
print(imgcv.shape)
final = imgcv.tostring()


# Set up callback functions
def on_connect(client, userdata, flags, rc):
    # When we connect to the broker, subscribe to the southernplayalisticadillacmuzik channel
    client.subscribe("config")
    client.subscribe("predict")
    client.subscribe("predict/results")


def on_message(client, userdata, message):
    # When we receive a message, print it out
    if(message.topic == "config"):{
     print("hi config")
    }
    if(message.topic == "predict"):
        options = {"model": "cfg/yolo.cfg", "load": "bin/yolov2-tiny.weights", "threshold": 0.1}
    if(message.topic=="predict/results"):
        print(message.payload)



# Connect callbacks to client
mqtt.on_connect = on_connect
mqtt.on_message = on_message
# print(np.array2string(imgcv))
# s =
# print(result)
# Connect and wait for messages
mqtt.connect()
a=cpickle.dumps(imgcv)



# finala =pack('=%sf' % imgcv.size, *imgcv.flatten('F'))
# print(str(a))
mqtt.publish("predict",a.hex(),0)
# print(np.array2string(imgcv.tostring()))
while (True):
    time.sleep(1000)  # wait for messages

