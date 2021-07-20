##
# Summer course in Applied IoT at Linnaeus University summer 2021 
# Kalle Friberg - km222tv
##
# Data from sensors are sent to Pybytes.
# Please configure WiFi and your device in Pybytes and use Pycom Firmware Updater to flash the device
# and register it on Pybytes, before running this code on your Pycom device.
##
# Code below comes from different places.
# check_plant: By David Agerberg, Edvin Hellsing and Joel Klingberg, from 2020
# lib/dht.py : Originally from https://github.com/JurassicPork/DHT_PyCom
# refactoring: Functions and inspiration from Leyla Wejdell: https://github.com/lwej/Pycom-Soil-Monitor/blob/master/test%20run/test.py
##
import time                 # Allows use of time.sleep() for delays
import machine              # Interfaces with hardware components
from dht import DHT         # Library for the DHT11 (or DHT22) Sensor
from machine import Pin     # Pin object to configure pins
from machine import ADC     # ADC object to configure reading values
##
ADC_PIN = 'P15'             # Pin for moisture sensor
DHT_PIN = 'P23'             # Pin for DHT sensor

# Function to print information about the plant's soil moisture
def check_plant(sensor_reading): 
    LOW_VALUE  = 30 # Definitions of break points values from the soil moist sensor
    HIGH_VALUE = 70
    if sensor_reading >= LOW_VALUE and sensor_reading <= HIGH_VALUE: # If value is between 1000-2500, print text below and activate green LED
        print("Woooa! Perfect, between {0}-{1} is the target range, you have green fingers my old friend!".format(LOW_VALUE, HIGH_VALUE))
    elif LOW_VALUE > sensor_reading: # If value is below 1000, print text below and activate yellow LED
        print("Hmm! Below {0} is too wet, drink the water instead of poring it over your flowers, else you will get blisters on your fingers.".format(LOW_VALUE))
    elif HIGH_VALUE < sensor_reading: # If value is over 2500, print text below and activate red LED
        print("Ooof! Over {0} is perhaps too dry, you should water your poor flowers.".format(HIGH_VALUE))
    else: # If an error is suspected, blink all LED lights and print text below
        print("Man, This is a tricky one, it might be a bit too dry or a bit too wet, or something spooky's happening. I have no idea what you should do.")

# Function to read value of a soil moisture sensor
def moist_sensor(pin):
    adc = ADC()             # ADC used to read data from A0
    apin = adc.channel(pin=pin, attn=ADC.ATTN_11DB)
    value = apin.value()
    return value

# Function to read values from the DHT11 sensor
def humid_temp_sensor(pin):
    th = DHT(pin, 0)        # Type 0 = dht11 Type 1 = dht22
    time.sleep(2)
    result = th.read()
    while not result.is_valid():
        time.sleep(.5)
        result = th.read()
    return (result.temperature, result.humidity)

while True:
    # Get the temp and humidity from the DHT sensor
    result = humid_temp_sensor(DHT_PIN)
    temperature = (result[0] * 100)     # Needs to be divided by 100 when displaying
    humidity = result[1]
    # Get the moisture from the moisture sensor
    result = moist_sensor(ADC_PIN)      # Grabs the sensor value
    moisture = ((result / 4096) * 100)  # Moisture = 100 % would be completely dry
    check_plant(moisture)               # Check plant reading and display information

    #Prints all sensor values
    print('Moisture: ' + str(moisture))
    print('Temperature:' + str(temperature/100))
    print('Humidity: ' + str(humidity))
    
    # Send sensor results to Pybytes with three separate signals
    pybytes.send_signal(1, (temperature/100))
    pybytes.send_signal(2, humidity)
    pybytes.send_signal(3, moisture)
 
    # The loop sleeps in X seconds. 30 seconds is only for development!
    time.sleep(30)
