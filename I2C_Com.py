# Raspberry Pi to Arduino I2C Communication 
# Python Code 
 
from smbus import SMBus
 
# Slave Addresses for Arduinos 
ARDUINO_1_ADDRESS = 0x04 # I2C Address of Arduino 1 
# ARDUINO_2_ADDRESS = 0x05 # I2C Address of Arduino 2 
# ARDUINO_3_ADDRESS = 0x06 # I2C Address of Arduino 3 
 
# Create the I2C bus 
I2Cbus = smbus.SMBus(1) 
 
# aSelect = input("Which Arduino (1-3): ") 
bSelect = '0' 
 
SlaveAddress = ARDUINO_1_ADDRESS 
# if aSelect == 1: 
#   SlaveAddress = ARDUINO_1_ADDRESS 
# elif aSelect == 2: 
#   SlaveAddress = ARDUINO_2_ADDRESS 
# elif aSelect == 3: 
#   SlaveAddress = ARDUINO_3_ADDRESS 
# else: 
#   # quit if you messed up 
#   quit() 
 
# also quit if you messed up 
# if bSelect != "on" or bSelect != "off": quit() 
 
BytesToSend = ConvertStringToBytes(bSelect) 
I2Cbus.write_i2c_block_data(SlaveAddress, 0x00, BytesToSend) 
print("Sent " + SlaveAddress + " the " + bSelect + " command.") 
 
# This function converts a string to an array of bytes. 
def ConvertStringToBytes(src): 
  converted = [] 
  for b in src: 
    converted.append(ord(b)) 
  return converted