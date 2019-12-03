import mh_z19
import time
import paho.mqtt.client as mqtt

while __name__ == '__main__':
  value = mh_z19.read()
  client = mqtt.Client()
  client.username_pw_set(username="username",password="password")
  client.connect("mqtt_ip",1883,60)
  client.publish("home/livingroom/co2", value["co2"])
  time.sleep(60)

