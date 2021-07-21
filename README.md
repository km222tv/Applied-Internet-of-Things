# Applied-Internet-of-Things
As part of the summer course at Linnaeus University, 1DT305 - Applied Internet of Things. 

This is where you can find the code for the IoT device which sends multiple sensor data streams to the Datacake cloud service via LoRaWAN and via Pybytes. 

For information about the project, and a tutorial how to set things up, please go to https://hackmd.io/RYcG7EvNRWOfEwmZIQfCDw.

In short, in the project I have used a Pycom LoPy4 microcontroller with some sensors for measuring the temperature, humidity and moisture in my greenhouse. 

The first part is to build and connect the microcontroller via WiFi to Pycom Pybytes, then integrate to Datacake for storage and displaying the data, and trigger alerts when values exceed predefined thresholds.

The second part is to connect it to The Things Stack (TTS) via my own LoRa gateway, and replicate the integration to Datacake from TTS.

/Kalle Friberg, km222tv
