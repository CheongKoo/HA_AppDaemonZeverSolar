# HA_AppDaemonZeverSolar
## Home Assistant - AppDaemon Application to extract generated power from Zeversolar inverter

This AppDaemon application gets the generated power from the ZeverSolar Inverter and shows it on a panel in HomeAssistant. This is done by accessing the URL for the Zeversolar unit, parsing this data and sending it to HomeAssistant using MQTT. Refer to (1) below for more information about the format of the ZeverSolar URL and the format of the returned data.

*Note that I am still very much a newbie with regards to programming in Python and AppDaemon. Any comments and suggestions would be appreciated.*

## Steps to setting it up
1. Install AppDaemon. Refer AppDaemon [instructions](https://appdaemon.readthedocs.io/en/stable/)
2. Download the python application zeversolarget.py from this repository and put it into the directory */config/appdaemon/apps/*
3. Remember to modify the above python file with the URL for your ZeverSolar inverter and the MQTT message structure.
4. Add into your */config/appdaemon/apps/apps.yaml* the entry for the new module and class in 2. See sample entry in this repository.
5. Add into your */config/configuration.yaml* the MQTT entry for ZeverSolar messages. See sample entry in this repository.
6. Remember to modify the MQTT entry to suit the changes from step 3.
7. Goto your Hass.IO AppDaemon add.on screen and you should be able to see some log messages.
```
2019-12-06 11:21:05.344670 INFO zever_solar: ----- Get Gen Callback -----
2019-12-06 11:21:05.382988 INFO zever_solar: Payload: {"power":"4.65"}
2019-12-06 11:21:05.433665 INFO zever_solar: Payload: {"datetime":"06/12/2019 11:21"}
2019-12-06 11:22:05.350457 INFO zever_solar: ----- Get Gen Callback -----
2019-12-06 11:22:05.395616 INFO zever_solar: Payload: {"power":"4.98"}
2019-12-06 11:22:05.451206 INFO zever_solar: Payload: {"datetime":"06/12/2019 11:22"}
```
8. If everything is working fine, you can now add this new entity to your Home Assistant overview screen. 

**Reference:**
1. [Reading ZeverSolar Inverter](https://forum.pvoutput.org/t/how-to-read-data-direct-from-zeversolar-inverter/1030/8)
2. [AppDaemon MQTT API reference](https://appdaemon.readthedocs.io/en/latest/MQTT_API_REFERENCE.html)
3. [AppDaemon instructions](https://appdaemon.readthedocs.io/en/stable/)
4. [AppDaemon API Reference](https://appdaemon.readthedocs.io/en/latest/AD_API_REFERENCE.html)


