import smbus

channel = 1 # Use the first channel of the I2C on RPI (GPIO PIN3)

STM_Addr = 0x00 # We need to get that using sudo i2cdetect -y 1 when connecting the STM
Reg_Addr = 0x06 # Register address to write to

bus = smbus.SMBus(channel)

bus.write_i2c_block_data(STM_Addr, Reg_Addr, 2) # Writes the value 2 to the device for testing