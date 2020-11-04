import smbus 
import time

bus = smbus.SMBus(1) # Use channel 1 for communication

STM_Addr = 0x06

def writeVal(value):
    bus.write_byte(address, value)
    return 0

while True:
    var = input("Enter a value: ")
    if not var:
        pass

    writeVal(var)
    print("Sent value: ", var)

