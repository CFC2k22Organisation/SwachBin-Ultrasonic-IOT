# SwachBin - Ultrasonic - IOT Module
import time
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

ORG = "lw59h1"
DEVICE_TYPE = "SwachBin"
TOKEN = ")whpKZC4BqD8b2c&l2"
DEVICE_ID = "e45f0142fbe8"
server = ORG + ".messaging.internetofthings.ibmcloud.com";
pubTopic1 = "iot-2/evt/Waste level/fmt/json";
authMethod = "use-token-auth";
token = TOKEN;
clientId = "d:" + ORG + ":" + DEVICE_TYPE + ":" + DEVICE_ID;

TRIG = 21
ECHO = 20
#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
print("Calibrating.....")
time.sleep(2)
mqttc = mqtt.Client(client_id=clientId)
mqttc.username_pw_set(authMethod, token)
mqttc.connect(server, 1883, 60)

while True:
       GPIO.output(TRIG, True)
       time.sleep(0.00001)
       GPIO.output(TRIG, False)
 
       while GPIO.input(ECHO)==0:
          pulse_start = time.time()
 
       while GPIO.input(ECHO)==1:
          pulse_end = time.time()
 
       pulse_duration = pulse_end - pulse_start
 
       distance = pulse_duration * 17150
       distance = round(distance+1.15, 2)
       
       mqttc.publish(pubTopic1, distance)
       print("published")
   
       time.sleep(5)
