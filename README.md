# Applied-Internet-of-Things
As part of the summer course at Linnaeus University, 1DT305 - Applied Internet of Things. This is where you can find the code for the IoT device which sends multiple sensor data streams to the Datacake cloud service via LoRaWAN and via Pybytes. 

Kalle Friberg, km222tv

The project is about learning hands-on how to build an end-to-end Internet of Things solution. 

I will use some sensors attached to a Pycom LoPy4 microcontroller for measuring the temperature, humidity and moisture in my greenhouse. Then connect via WiFi and LoRa to Pybytes and The Things Network (TTN) respectively, and integrate to Datacake for storage and displaying the data, and trigger alerts when values exceed predefined thresholds.

The time needed to replicate the project is roughly estimated to:
| Phase                         | Est. time |
| -----                         | ------ |
| Flash (update/erase) the LoPy4| 1 h    |
| Set up the computer           | 1 h    |
| Build the device with sensors | 1 h    |
| Coding (avail. from Github)   | 1 h    |
| Connect via WiFi to Pybytes   | 1 h    |
| Integrate Pybytes to Datacake | 0.5 h  |
| Build dashboard in Datacake   | 1.5 h  |
| **Sum WiFi & Pybytes**        |**7 h** |
| | |
| Set up my own Pycom gateway   | 2.0 h  |
| Connect via LoRa to TTN       | 1.5 h  |
| Integrate TTN to Datacake     | 1.5 h  |
| Build dashboard in Datacake   | 1.0 h  |
| **Additional for LoRa & TTN** |**4 h** |

## Objective

As part of the summer course at Linnaeus University, 1DT305 - Applied Internet of Things - Introduction, I chose to build a device to send multiple sensor data streams, using the recommended LoPy4 microcontroller from Pycom, to the Datacake cloud service.

The second part is to use LoRa and, via my own gateway and The Things Stack, forward the sensor data to Datacake.

The purpose is to understand Internet of Things from end to end, by building an end-to-end IoT solution to keep track of my greenhouse environment, and use this knowledge to build more IoT solutions for my house.

I aim to give me and others the experience and insights on both which areas are necessary for building a complete solution, which different alternatives are available for each area, and which of these I would like to focus on in the future:
- Sensors and device logic for different use cases,
- Choice of network/s and how to connect, or
- Platforms for storage, visualisation and alerts

## Material
In this project I have chosen to work with the Pycom LoPy4 device as seen in Fig. 1.
![LoPy!](https://pycom.io/wp-content/uploads/2018/08/lopySide-1.png =360x)
Fig. 1. LoPy4 without the extension board. Pycom.io

To build the device, I am using two sensors; 
- DHT11, for temperature and humidity ([Link to PDF](https://www.electrokit.com/uploads/productfile/41015/41015728_-_Digital_Temperature_Humidity_Sensor.pdf))
- Moisture sensor, for moisture level in soil ([Link to PDF](https://www.electrokit.com/uploads/productfile/41015/41015738_-_Soil_Moisture_Sensor.pdf))

The DHT and moisture sensors are mounted on a breadboard and wires are connected to the Pycom expansion board, on which the LoPy4 microcontroller is mounted.

The LoPy4 is the brain, which you can program and to connect to networks, using external or built-in antennas, while the expansion board is used to connect to the sensors, using wires for voltage and data.

As both sensors already have built-in resistors, the solution I'm building don't need separate ones.

Please see below, in the 'Putting everything together' section, how the items are connected.

For the second part, I have bought a Pycom Pygate for use as my own LoRa gateway, connected to The Things Stack.

### List of material
| IoT Thing | Cost       | Where to buy |
| --------- | ---------------- | -- |
| LoPy4 bundle, incl. Pycom expansion board, LoRa antennae, breadboard, USB cable, LEDs, resistors, wiring, etc. | ~1000 SEK | electrokit.com |
| Sensor kit 25 modules (optional) | 325 SEK | electrokit.com |
| Pygate, incl. WiPy, Ethernet module, case and antennae (optional) | ~1600 SEK | pycom.io |

## Computer setup
In order for the LoPy4 to read data from your sensors and send them to the server of choice, you need to be able to program it with MicroPython, by following the following steps.

### Update the Pycom firmware
It is good practice to ensure that the firmware is updated with the latest version, to avoid spending time on already fixed bugs.
1. Start by plugging the LoPy4 board into a Pycom Expansion board and connecting that to your computer with a Data USB cable.
![](https://i.imgur.com/pzNVmdC.jpg)
Fig. 2. LoPy4 mounted on the Pycom Expansion board and a Data USB cable. (ADD NEW PICTURE)
2. Download the Pycom Firmware Updater from https://pycom.io/downloads and follow the instructions when installing it on your computer.
3. When installed, start the Pycom Firmware Update app.
4. In the Communication step, the app should have found the port connected to the device, e.g., COM3. Check the 'Show Advanced Settings' before clicking Continue.
5. In the Advanced Settings step, check the 'Erase during update' option so old files and configurations on the LoPy4 don't interupt your work going forward. Then choose Continue.
![](https://i.imgur.com/Qt7hIqo.png)
Fig. 4. Check the 'Erase during update' option.
6. Wait while the app is upgrading, until it displays 'Result', then copy the unique 'Device ID' for use later.

You should now have ensured the LoPy4 has the latest firmware version.

### Installing VS Code as IDE
As IDE I have chosen Microsoft VS Code, because I have used it before and because of the extension support for working with Azure, which I think I will use for my IoT devices in the future. 
1. Download from https://code.visualstudio.com/Download.
2. Start the Installer, accept the agreement and click Next until you reach the 'Ready to Install' page, where you click Install and wait for it to finish.

### Installing Node.js
To use the Pymakr extension in VS Code, you need node.js installed on your computer, and it's recommended that you do this first.
1. Download the Long-Term Support version of Node.js from https://nodejs.org/en/ 
2. Start the installation (Setup Wizard) and click Next until you reach the 'Ready to Install' page, where you click Install and wait for it to finish.

### Install the Pymakr VSCode Extension
Pycom supports Microsoft’s Visual Studio Code IDE platform with the Pymakr extension, as mentioned [on their site](https://docs.pycom.io/gettingstarted/software/vscode/):
> Pymakr enables you to communicate to your Pycom board using the build in command line REPL. The Pymakr Plugin adds a REPL console to the terminal within VS Code, that connects to your Pycom board.
1. Open VS Code and go to the Extensions tab. 
2. Search for, and install, Pymakr.
![](https://i.imgur.com/dMr86OJ.png)
Fig. 6. Install the Pycom Pymakr extension in VS Code, after installing Node.js.

Now everything you need is in place for you to start writing and uploading programs to the device.

### Test the device
Before you write and upload your own program to the LoPy4, you can test the device by trying out the 'RGB LED' code from https://docs.pycom.io/tutorials/basic/rgbled/:

1. Connect the Data USB cable to your computer.
2. Open the Command Prompt on your computer and create a folder on your computer (mkdir) and change into that folder (cd), in my example C:\repos\pymakr\rgb.
3. Write "code ." and press Enter, to open VS Code in that folder. This assumes you have added VS Code to the PATH.
![](https://i.imgur.com/J5iGuKL.png)
Fig. 7. Create a folder and open VS Code in that folder, using Command Prompt.
4. In VS Code, ensure that the Pymakr extension loads the Pymakr Console, and that the device is connected to a COM port.
![](https://i.imgur.com/IFHaJqm.png)
Fig. 8. VS Code with Pymakr Console loaded and COM3 connected, displaying the REPL '>>>'.
5. Click on 'Download' in the status bar, and answer 'Yes' to create two empty files in the RGB folder:
-- boot.py – can be empty.
-- main.py – where you should paste in the code shown above.
These files were created when you updated the Pycom firmware with the 'Erase during update' option.
Note: If you get an error in the Pymakr Console, e.g., *"Download failed.: timeout Please reboot your device manually."*, remove and attach the USB cable, and try again.
6. Paste in the code from https://docs.pycom.io/tutorials/basic/rgbled/ in main.py, and don't forget to save it!
7. In the status bar, this time click on 'Upload', to write the updated files back to the LoPy4.
The program should automatically start and you should see the light on the microcontroller change colour between green, yellow and red.
9. After a while, the program will stop, and the red colour is turned on permanently, since that is the last colour in the loop.

## Putting everything together
Since the project includes two sensors; a Humidity & temperature sensor (DHT11), and a Soil moisture sensor, I have used a breadboard, which '+' and '–' rows are connected to the 3V3 (power) and the GND (ground), respectively.
In the circuit diagram below, the power wires (red), the ground wires (purple) and the data wires (yellow) are visible.
![](https://i.imgur.com/fA3nlPT.png)
Fig. 9. Circuit diagram using Fritzing.

1. For each sensor, connect the power pin to the + row, and the ground pin to the – row, on the breadboard.
2. Connect pin P15 on the Pycom to 'A0' on the sensor, to get the data from the Soil Moisture.
3. Connect pin P23 on the Pycom to the left-most pin on the sensor, to get the data from the DHT.
4. Finally, connect the 3V3 (power) to the lower '+' row on the breadboard, and the GND (ground) to the '–' row.

![](https://i.imgur.com/HiIowhy.png)
Fig. 10. The setup in real life, powered by my Dormy Solar charger.

I have not done electrical calculations or used resistors, because this solution is only for a development setup, and both sensors already have built-in resistors and do not require separate ones, looking at the specifications: 
- DHT11, for temperature and humidity ([Link to PDF](https://www.electrokit.com/uploads/productfile/41015/41015728_-_Digital_Temperature_Humidity_Sensor.pdf))
- Moisture sensor, for moisture level in soil ([Link to PDF](https://www.electrokit.com/uploads/productfile/41015/41015738_-_Soil_Moisture_Sensor.pdf))

### Battery life and choice of communication
However, it is possible to roughly calculate the the battery life, and choose how to connect to the Internet based on the situation.

In my project, I am using both WiFi and LoRa. The main pros and cons are these:
| | WiFi | LoRa |
| - | - | - |
| Pros | High data rate | Long range and Low battery consumption|
| Cons | Short range and High battery consumption | Low data rate |

Since the project is only using small amounts of data, and the need for sending the data is not continuous, the primary choice is LoRa (ADD REF).

But, it could be useful to program a fallback to WiFi in your device, when the LoRaWAN network is (temporarily) not available. Especially if the device is in range of your WiFi router and powered by a solar charger.

## Platform
In this project I have successfully set up three routes:
* Connection via WiFi to Pybytes, and an integration to Datacake.
* Connection using LoRa and my own gateway connected to The Things Stack, and a second integration to Datacake.

In the following sections, I will go through how these are set up and discuss them.

### WiFi and Pybytes
First off is the connection to Pybytes using the microcontroller's WiFi functionality.

Programming the LoPy4 to connect to your WiFi, and send sensor data to Pybytes, is relatively easy, but Pybytes has limited support to store and visualise the data.

Another drawback from selecting Pybytes to connect your devices is the lack of an efficient support for scaling your solution, e.g., if you want to deploy hundreds of devices there will be much manual work.

However, Pybytes supports integrations directly to several known IoT solutions, e.g., Microsoft Azure, and using webhooks to whichever endpoint you want, in this project - Datacake, as described below.

#### How to connect via WiFi to Pybytes
Follow these steps to be able to send data to Pybytes over your WiFi.
1. Create an account with Pybytes and login.
![](https://i.imgur.com/PGGHTpU.png)
Fig. 11. Pybytes landing page after logging in. 
2. Add your WiFi credentials to Pybytes using 'Configure Networks'.
![](https://i.imgur.com/S7yOrSf.png)
Fig. 12. WiFi credentials are needed for the configuration file created in step 5.
3. Choose 'Add device' and select the WiFi option.
![](https://i.imgur.com/lpXG2gx.png)
Fig. 13. After adding the the device, copy the Activation Token from the 'Provisioning' / 'Offline Firmware Updater' tab. 
If you do this later, you can use the 'Generate New Activation Token' button.
4. Connect the device to your computer using a Data USB cable.
5. Run the Pycom Firmware Updater app, but this time you should check both 'Force update Pybytes registration' and 'Enable Pybytes / SmartConfig support' options, in the Communication step.
![](https://i.imgur.com/m148tjV.png)
Fig. 14. Check both options below the 'Pybytes' dropdown. 
6. In the Pybytes registration step, enter the Activation Token copied earlier, and click 'Continue' to finish the update of the LoPy4.
![](https://i.imgur.com/8dchlL2.png)
Fig. 15. Paste the Activation Token from step 3.

Now, you have registered your device in Pybytes, and created a configuration file on the device.

#### Try the connection to Pybytes out
Next, open VS Code in an empty folder, and download the created files from the device:
1. Connect the device to your computer using a Data USB cable.
2. Create a new folder using the Command prompt and change into that folder, e.g., C:\repos\pymakr\pybytes
3. Write "code ." to start VS Code in that folder.
4. Ensure Pymakr Console is starting and the connection is working, then click on 'Download' and answer 'Yes' to download the files into the folder:
![](https://i.imgur.com/jjTAlEU.png)
Fig. 16. You should also see in the Pymakr Console that the device tries to connect to your Wifi using the downloaded 'pybytes_config.json' file you configured in Pybytes before, as it is run automatically.

#### Upload the code to read and send sensor data
Now that you have tested that the device can connect to Pybytes, it's time to upload the code for sending the actual sensor data.

1. Configure the device with the sensors as described in the 'Putting everything together' section, and attach the Data USB cable.
2. Use the code available in the Code section, below, for the two sensors, DHT and Moisture sensor, and add them to the 'pybytes' folder:
    * lib/dht.py (place the dht.py file in a folder called 'lib')
    * main.py (replace the empty file from previous section)
    * boot.py (empty, unchanged from previous section)
    * pybytes_config.json (unchanged from previous section)
3. Be sure to save the files and click 'Upload' in the status bar in VS Code. The device should automatically connect, and run the program.
4. Go to Pybytes to see the result, which should be showing three signals:
-- 1 = Temperature from DHT
-- 2 = Humidity from DHT
-- 3 = Soil moisture from the Moisture sensor.
![](https://i.imgur.com/iYO2vgb.png)
Fig. 19. Using the same device as registered in Pybytes in the previous section, you should now see three signals, temperature, humidity and moisture.

As the storage and the presentation of data are limited, we need to integrate Pybytes to a better IoT solution platform for storing long time series and present it, in my project - to Datacake.

### Integrate to Datacake
This section explains how to set up Datacake for integration from Pybytes and display the three signals originated from your device.

Datacake has an [overview guide](https://docs.datacake.de/integrations/webhook), but for the project you can follow these steps:
1. Create an account with Datacake and login.
2. Add a new device, and in step 1 (Product), choose API -> New product from template -> Pycom Pybytes base template.
3. In step 2 (Devices), add the GUID which shown under the name of the device in Pybytes, in the 'Serial number' field, and a name for the device, in Datacake.
![](https://i.imgur.com/O9Makyh.jpg)
Fig. 20. Use the device ID from Pybytes when adding a device in Datacake. 
4. In step 3 (Plan), choose Free, and click on 'Add 1 device'.
5. When the API has been created in Datacake, go to the device's API configuration page and **copy** the 'HTTP Endpoint URL'.
6. Go back to Pybytes and create a new Webhook integration the Integration section.
7. In the 'URL' field, **paste** the HTTP Endpoint URL from Datacake.
![](https://i.imgur.com/Y0GPKgE.png)
Fig. 21. There is a known error in Pybytes, which strips the URL so the last forward slash "/" is removed when saving. To resolve this, add "/ignore" in the end of it before saving.
8. Choose a 'Webhook Event Name' like "Datacake" and **in the bottom of the page**, check the checkbox of your device before clicking on Create.

The integration to Datacake should now be successfully created, and you can run your device to see the data received in Datacake.

#### Create a dashboard in Datacake
Try the different widgets out, available in Datacake, and configure them for the signals received from Pybytes. 
![](https://i.imgur.com/YcAemph.png)
Fig. 22. This is my dashboard in Datacake, displaying the sensor data.

#### Create a rule in Datacake
The last piece is setting up a rule which sends an email if the soil is too dry.

Follow these steps:
1. Go to the Rules section of Datacake and create a new rule.
2. Add a name, conditions and (in this case) what should be included in the mail.
![](https://i.imgur.com/7RxeLNL.png)
Fig. 23. A rule in Datacake which is triggered when the moisture of the soil is over the value of 3000.
NOTE: 'Hysteresis' means that the measurement must come below that value (in this case 2800) in order for the rule to be triggered a second time.
3. Take the moisture sensor out of the soil to fake a very dry value, and see if you get an email.
![](https://i.imgur.com/F4WO0cm.png)
Fig. 24. An email received from Datacake when my "soil" was too dry.

### Using my own LoRa gateway
The second part of the tutorial is about LoRa, and since I can't currently connect to any public gateway to connect via LoRaWAN to The Things Stack, I have bought and assembled my own Pycom Pygate.

It's of course a bit expensive, but once you have it, there are some benefits:
* The connection to The Things Stack is very fast
* The so called 'Spread factor' should be in the very low end (7) as it is close, which saves battery on the devices you have in or around your house.

#### Setting up my own Pygate
When I ordered Pygate from Pycom, it arrives in 4-5 pieces, which should be assembled:
* The Pygate itself, which is a type of expansion board.
* A microcontroller, I chose the least expensive - WiPy 3.0 with headers, which you attach to the Pygate.
* A LoRa (868MHz/915MHz) & Sigfox Antenna Kit.
* A Pygate case, to assemble everything in.
* And, optionally, a Power over Ethernet Adapter module, if you want to use a wire instead of WiFi.

When assembled, follow these steps:
1. First thing is to update the firmware, which you do just as above for the LoPy4, including the creation of pybytes_config.json, but instead of selecting 'Pybytes', choose 'Pygate', in the Pycom Firmware Updater!
In the finishing screen, copy the Device ID, e.g., "2462abf4e3bc".
![](https://i.imgur.com/4ZdpxU1.png)
Fig. 24. Copy the Device ID.
3. Go to The Things Stack, and register your Pygate under 'Gateways', and in setting the 'Device EUI' enter the first 6 + '**FFFE**' + last 6 of the Device ID copied in the previous step, e.g., "2462ab**FFFE**f4e3bc". 
You can read more about the Gateway EUI [here](https://www.thethingsindustries.com/docs/reference/glossary/#gateway-eui).
4. Next, upload the code you can find in the Code section below for the Pygate, including changing the "Gateway_ID" in config.json to you own value, e.g., "2462AB**FFFE**F4E3BC".
> The code should automatically run, and if successfully showing up in The Things Stack, you can now move your Pygate to any micro USB cable to start it up.

Now, the gateway should be working and be possible to connect to from your sensor devices.

#### The Things Stack
To be able to forward the data packets from the gateway to Datacake, you need to create an application and add an 'End device' to that application in The Things Stack (TTI), which represents your sensor device.

Alternatively, when using LoRa, you could connect to Helium instead of TTI, but the cost-free TTI is enough for my purposes with lower requirements for e.g., security.

Follow these steps:
1. Attach your LoPy4 device with a Data USB cable.
2. Follow the same steps you can find in the 'Update the Pycom firmware' instructions in the beginnging of this tutorial.
3. In the finishing screen, copy the Device ID, e.g., "70B3D5499412CFBC".
4. Create an application, e.g., "my-iot-app", with a descriptive name.
5. Register an end device and choose the 'Manually' tab, 'Over the air activation (OTAA)' and 'MAC v1.0.2' LoRaWAN version.
6. In step 1 (Basic), enter an ID, e.g., "my-sensor-device", App EUI (can be just zeros), the Dev EUI which you should get from when you updated the firmware above.
7. In step 2 (Network), use the recommended 'Frequency plan' and the REV A as 'Regional parameters version'.
8. In step 3 (Join), generate a new 'App Key', and click 'Add end device'. 
9. When registered, copy the 'App Key' from the 'Overview' tab.
This App Key needs to be used in the boot.py file, which you can find in the Code section below.
9. Upload the code for the LoPy4, including your own App Key, to the device, and test that it sends data to TTI.

#### Integrate to Datacake, again
To present the data in Datacake using LoRa and The Things Stack, you need to create a new integration to Datacake.

Follow these steps:
1. Login to Datacake, where you should create your second - free - device with the Device EUI from previous section.
2. When created, go to the Configuration tab and add the following 3 fields:
![](https://i.imgur.com/LxB83zH.png)
Fig. 25. Add Temperature, Humidity and Moisture as fields in the Datacake device configuration tab.
3. Add the Decoder javascript code from the Code section below, into the Payload decoder section, on the same tab.
4. Before going to TTI to set up the integration, you need to create an API token in Datacake, which you do on under the 'Members' menu and 'API Users' tab. Be sure to check 'Devices' and under Permissions: 'Can record measurements'! Then copy the API token.
5. In TTI, go to the 'Integrations'/'Webhooks' menu and add a new Webhook of the type 'Datacake'. Fill in a Webhook ID, e.g., "datacake-webhook" and paste in the API token.
Now, all sensor data should be forwarded to Datacake.
6. As before, when integrating from Pybytes, you can now set up your dashboard for displaying what the three sensors are reading.

## Discussion about platforms and devices
For the IoT solution to work with low power consumption over time, LoRa is preferable to WiFi, and using The Things Stack works very well to forward packages to your platform of choice.

In this development setup, the two free devices work fine using Datacake, and as it's a reasonable fee for a production environment, I will probably compare Datacake and MS Azure IoT Hub for my future solutions.

I have decided to use cloud solutions such as Pybytes, The Things Stack and Datacake, to be able to focus on the functionalities and not having to operate a service on my own environment such as the TIG stack.

Regarding the devices, building and programming your own device has been very instructive, but unless I can't find the device I need, I will look at off-the-shelf sensor and actuating products to set up.

Finally regarding the gateway, the Pygate will be useful for now, and it might be I will prefer having my own even when public gateways become available where I live, to keep having control over the infrastructure. However, as with many things cloud services will most probably be more reliable over time, so we will see about that.

## The code
Please go to GitHub, to find the code for 
* For the LoPy4 device using WiFi and Pybytes [Link to GitHub](https://github.com/km222tv/Applied-Internet-of-Things/tree/main/pybytes)
* For the LoPy4 device using a LoRa gateway and The Things Stack [Link to GitHub](https://github.com/km222tv/Applied-Internet-of-Things/tree/main/lorawan)
* For the Pygate [Link to GitHub](https://github.com/km222tv/Applied-Internet-of-Things/tree/main/pygate_gw)
* For the Datacake Payload decoder configuration [Link to GitHub]([link](https://github.com/km222tv/Applied-Internet-of-Things/tree/main/datacake_decoder))
