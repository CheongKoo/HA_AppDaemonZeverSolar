# File: zeversolarget.py
# Author: Cheong Koo
# 
# Description: Home Assistant AppDaemon application to get solar generated power
# from ZeverSolar inverter and send it to the front end using MQTT.
# Callback function to update reading every minute.
#
# Modify MQTT payload format to match with your MQTT settins in Home Assistant.
#
# Reference: ZeverSolar https://forum.pvoutput.org/t/how-to-read-data-direct-from-zeversolar-inverter/1030/2

import appdaemon.plugins.hass.hassapi as hass
import urllib.request
import datetime

# ---------------------------------------------------------------------
# Global variables
# ---------------------------------------------------------------------
link = "http://192.168.1.XXXX/home.cgi"  # Fill in IP address of ZeverSolar Inverter
myDatetime = "dd/mm/yyyy hh:mm"
myGeneration = "0.00"
myDailykWh = "0.00"

from urllib.request import Request, urlopen
from urllib.error import  URLError
from datetime import datetime
from datetime import timedelta

class ZeverSolar(hass.Hass):
    def initialize(self):
        self.log("------------------------------------------------")
        self.log("Initiatilize: Get energy from solar system.")
        # Register call back function for every 1 minute
        # Delay callback by 5 mins from start        
        startTime = datetime.now() + timedelta(minutes=5)
        self.handle = self.run_every(self.doGetGenAndSendMQTT,  startTime, 1 * 60)

    # Get generation and send out message
    def doGetGenAndSendMQTT(self, arg):
        global myDatetime
        global myGeneration
        global myDailykWh
      
        self.log("----- Get Gen Callback -----")
        self.requestSolarGeneration(self)
        # Send generated power
        myTopic = "home/solargen/POWER"  # MQTT topic for generated power
        myPayload = "{\"power\":" + "\"" + myGeneration + "\"}"
        self.log("Payload: " + myPayload)  # MQTT payload for generated power
        self.call_service("mqtt/publish", topic = myTopic, payload = myPayload)
        # Send date and time of reading
        myTopic = "home/solargen/DATETIME" # MQTT topic for time of reading
        myPayload = "{\"datetime\":" + "\"" + myDatetime + "\"}"
        self.log("Payload: " + myPayload)  # MQTT payload for time of reading
        self.call_service("mqtt/publish", topic = myTopic, payload = myPayload)
        # Send total generated kWh
        myTopic = "home/solargen/DAILYKWH" # MQTT topic for daily kWh
        myPayload = "{\"dailykwh\":" + "\"" + myDailykWh + "\"}"
        self.log("Payload: " + myPayload)  # MQTT payload for generated power
        self.call_service("mqtt/publish", topic = myTopic, payload = myPayload)

    # Returns a string containing the generation or 0 if an error
    def requestSolarGeneration(self, arg):
        global myDatetime
        global myGeneration
        global myDailykWh
      
        now = datetime.now()
        myDatetime = now.strftime("%d/%m/%Y %H:%M")  # dd/mm/YY H:M:S
        req = Request(link)
        try:
            response = urlopen(req)
            htmlresponse = response.read()
            st = htmlresponse.decode()
            st = st.split()
            gen = st[11]
            totgen = st[12]
            txt = "{:.2f}"
            myGeneration = txt.format(float(gen)/1000)
            myDailykWh = txt.format(float(totgen))
            return
        except:
            self.log("Error in connecting to Zever solar server")
            myGeneration = "0.00"
            return
