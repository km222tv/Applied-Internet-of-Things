##
# Summer course in Applied IoT at Linnaeus University summer 2021 
# Kalle Friberg - km222tv
##
# Data from sensors are sent via LoRaWAN to The Things Stack
# Connection to TTS is done in boot.py, after which main.py is run.
##
# Code below comes from https://docs.pycom.io/tutorials/networks/lora/lorawan-otaa/
##
from network import LoRa
import time
import binascii

# Initialise LoRa in LORAWAN mode.
# Please pick the region that matches where you are using the device:
# Asia = LoRa.AS923
# Australia = LoRa.AU915
# Europe = LoRa.EU868
# United States = LoRa.US915
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

# Uncomment for US915 / AU915 & Pygate
# for i in range(0,8):
#     lora.remove_channel(i)
# for i in range(16,65):
#     lora.remove_channel(i)
# for i in range(66,72):
#     lora.remove_channel(i)

# Create an OTAA authentication parameters, change them to the provided credentials
app_eui = binascii.unhexlify('0000000000000000')
app_key = binascii.unhexlify('101CF5923A25FC5A49BCE83BBEB37A22') # Add your own APP_KEY here
# Uncomment to use LoRaWAN application provided dev_eui
# dev_eui = ubinascii.unhexlify('70B3D549938EA1EE')

# Join a network using OTAA (Over the Air Activation)
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

# Wait until the module has joined the network
while not lora.has_joined():
    time.sleep(2.5)
    print('Not yet joined...')

print('Joined')
