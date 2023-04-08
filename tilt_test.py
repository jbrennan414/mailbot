import time
import board
import digitalio
import adafruit_lis3dh
i2c = board.I2C()
int1 = digitalio.DigitalInOut(board.D6)  # Set this to the correct pin for the interrupt!
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, int1=int1)

x, y, z = lis3dh.acceleration
print(x,y,z)
