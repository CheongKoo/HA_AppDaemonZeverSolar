# HA_AppDaemonZeverSolar
**Home Assistant - AppDaemon Application to extract generated power from Zeversolar inverter**

This AppDaemon application gets the generated power from the ZeverSolar Inverter and shows it on a panel in HomeAssistant. This is done by accessing the URL for the Zeversolar unit, parsing this data and sending it to HomeAssistant using MQTT. Refer to (1) below for more information about the format of the ZeverSolar URL and the format of the returned data.

*Note that I am still very much a newbie with regards to programming in python and AppDaemon. Any comments and suggestions would be appreciated.*

The tricky areas that I had to overcome were:
* Handling the scenario when ZeverSolar website was down. This occurs during the night when there is no generated power to the unit.
* Integrating it with HomeAssistant AppDaemon. 

**Steps**
WIP ... (need to put in code and instructions)


**Reference:**
1. [Reading ZeverSolar Inverter](https://forum.pvoutput.org/t/how-to-read-data-direct-from-zeversolar-inverter/1030/8)
2. [MQTT API reference](https://appdaemon.readthedocs.io/en/latest/MQTT_API_REFERENCE.html)
3. [AppDaemon API Reference](https://appdaemon.readthedocs.io/en/latest/AD_API_REFERENCE.html)


