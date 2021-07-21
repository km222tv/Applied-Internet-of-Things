# Applied-Internet-of-Things
As part of the summer course at Linnaeus University, 1DT305 - Applied Internet of Things. 

This is where you can find the code for the IoT device which sends multiple sensor data streams to the Datacake cloud service via LoRaWAN and via Pybytes. 

For information about the project, and a tutorial how to set things up, please go to https://hackmd.io/RYcG7EvNRWOfEwmZIQfCDw.

## The project
In short, in the project I have used a Pycom LoPy4 microcontroller with some sensors for measuring the temperature, humidity and moisture in my greenhouse. 

The first part is to build and connect the microcontroller via WiFi to Pycom Pybytes, then integrate to Datacake for storage and displaying the data, and trigger alerts when values exceed predefined thresholds.

The second part is to connect it to The Things Stack (TTS) via my own LoRa gateway, and replicate the integration to Datacake from TTS.

This is a short information about the code you can find in the GitHub repository.
* For the LoPy4 device using WiFi and Pybytes ([Link](https://github.com/km222tv/Applied-Internet-of-Things/tree/main/pybytes))
    * After adding your WiFi details and your device in Pybytes, copy the Activation Token from the device's Provisioning -> Offline firmware updater tab. This is important for creating the pybytes_config.json file, needed to connect to your WiFi and also to send the data correctly to Pybytes.
    * Run the Pycom Firmware Updater to reset the microcontroller (e.g., LoPy4) and create the files on the device. In the 'Communication' step, check both Pybytes checkboxes, and paste the Activation Token in when asked.
    * With Atom or VS Code with the Pymakr extension, download the files which were created on the device; boot.py, main.py and pybytes_config.json, to an empty, local folder on your computer.
    * From this repository, **add** the lib/dht.py and **replace** the main.py, save and upload to the device, then the code should run automatically.
* For the LoPy4 device using a LoRa gateway and The Things Stack ([Link](https://github.com/km222tv/Applied-Internet-of-Things/tree/main/lorawan))
    * Run the Pycom Firmware Updater to reset the microcontroller (e.g., LoPy4) and create the files boot.py and main.py on the device. In the 'Communication' step, do not check the Pybytes checkboxes, but in the last screen, copy the Device ID, e.g., "70B3D5499412CFBD".
    * In The Things Stack, create an application, e.g., "my-iot-app", and register an end device using the 'Manually' tab, e.g., "my-sensor-device". The Device ID you copied should be pasted in to the Dev EUI.
    * When the device is registered, copy the 'App Key' from the 'Overview' tab and use it later in the boot.py file.
    * With Atom or VS Code with the Pymakr extension, download the files which were created on the device; boot.py and main.py, to an empty, local folder on your computer.
    * From this repository, **add** the lib/dht.py and **replace** both the boot.py and main.py files.
    * Use the 'App Key' from earlier and paste it into the boot.py file, save the files and upload to the device, then the code should run automatically.
* For your own Pycom Pygate LoRa gateway ([Link](https://github.com/km222tv/Applied-Internet-of-Things/tree/main/pygate_gw))
* For the Datacake Payload decoder configuration ([Link]([link](https://github.com/km222tv/Applied-Internet-of-Things/tree/main/datacake_decoder))

/Kalle Friberg, km222tv
