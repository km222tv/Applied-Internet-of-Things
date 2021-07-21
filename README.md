# Applied-Internet-of-Things
As part of the summer course at Linnaeus University, 1DT305 - Applied Internet of Things. 

This is where you can find the code for the IoT device which sends multiple sensor data streams to the Datacake cloud service via LoRaWAN and via Pybytes. 

For information about the project, and a tutorial how to set things up, please go to https://hackmd.io/RYcG7EvNRWOfEwmZIQfCDw.

## The project
In short, I have built a device with the Pycom LoPy4 microcontroller and two sensors for measuring the temperature, humidity and moisture in my greenhouse.

The next part was to connect the device via WiFi to Pycom Pybytes, then integrate from there to Datacake to display the data in a dashboard and triggering alerts when values exceed predefined thresholds.

Finally, I bought and set up a Pycom Pygate LoRa gateway, to be able to connect the sensor device to The Things Stack (TTS), from which I set up a new integration to Datacake.

## The code
This is a short information about the code you can find in the GitHub repository.
* For the LoPy4 device using WiFi and Pybytes ([Link](https://github.com/km222tv/Applied-Internet-of-Things/tree/main/pybytes))
    * After adding your WiFi details and your device in Pybytes, copy the Activation Token from the device's Provisioning -> Offline firmware updater tab. This is important for creating the pybytes_config.json file, needed to connect to your WiFi and also to send the data correctly to Pybytes.
    * Run the Pycom Firmware Updater to reset the microcontroller (e.g., LoPy4) and to create the files on the device. In the 'Communication' step, check both Pybytes checkboxes, and paste the Activation Token in when asked.
    * With Atom or VS Code with the Pymakr extension, download the files which were created on the device; boot.py, main.py and pybytes_config.json, to an empty, local folder on your computer.
    * From this repository, **add** the lib/dht.py and **replace** the main.py, save and upload to the device, then the code should run automatically.
* For the LoPy4 device using a LoRa gateway and The Things Stack ([Link](https://github.com/km222tv/Applied-Internet-of-Things/tree/main/lorawan))
    * Run the Pycom Firmware Updater to reset the microcontroller (e.g., LoPy4) and to create the files boot.py and main.py on the device. In the 'Communication' step, do not check the Pybytes checkboxes, but in the last screen, copy the Device ID, e.g., "70B3D5499412CFBD".
    * In The Things Stack, create an application, e.g., "my-iot-app", and register an end device using the 'Manually' tab, e.g., "my-sensor-device". The Device ID you copied should be pasted in to the Dev EUI.
    * When the device is registered, copy the 'App Key' from the 'Overview' tab and use it later in the boot.py file.
    * With Atom or VS Code with the Pymakr extension, download the files which were created on the device; boot.py and main.py, to an empty, local folder on your computer.
    * From this repository, **add** the lib/dht.py and **replace** both the boot.py and main.py files.
    * Use the 'App Key' from earlier and paste it into the boot.py file, save the files and upload to the device, then the code should run automatically.
* For your own Pycom Pygate LoRa gateway ([Link](https://github.com/km222tv/Applied-Internet-of-Things/tree/main/pygate_gw))
    * Run the Pycom Firmware Updater to reset the microcontroller on your Pygate, and to create the files boot.py and main.py on the device. In the 'Communication' step, choose "Pygate" instead of "Pybytes" in the dropdown, and in the last screen, copy the Device ID, e.g., "2462acf4e3bc".
    * In The Things Stack, register your Pygate under Gateways, and in setting [Device EUI](https://www.thethingsindustries.com/docs/reference/glossary/#gateway-eui), paste the first 6 + '**FFFE**' + last 6 of the Device ID copied in the previous step, e.g., "2462AC**FFFE**F4E3BC".
    * With Atom or VS Code with the Pymakr extension, download the files which were created by the firmware updater on the device; boot.py and main.py, to an empty, local folder on your computer.
    * From this repository, **add** the config.json file and **replace** the main.py file.
    * Change the "Gateway_ID" in config.json to you own value, e.g., "2462AC**FFFE**F4E3BC", and - if you use WiFi - enter the SSID and password in the main.py file, save the files and upload to the device.
    * The code should run automatically, and if successfully showing up as a gateway in The Things Stack, you can now move your Pygate to any USB-C cable to start it up.
* For the Datacake Payload decoder configuration ([Link](https://github.com/km222tv/Applied-Internet-of-Things/tree/main/datacake_decoder))
    * When having registered your device in Datacake, create the following three fields on the device configuration tab; Humidity, Temperature and Moisture, to be able to store the sensor data values.
    * The javascript code should be pasted into the Payload decoder section, on the same tab.
    * Comment: The script is handling the raw payload coming from The Things Stack (originally from the struct in [main.py, line 73](https://github.com/km222tv/Applied-Internet-of-Things/blob/main/lorawan/main.py)) and devides it into the three values which are then stored in the Datacake fields. 

All code is also commented to describe what is done, where clarifications are needed.

/Kalle Friberg, km222tv
