import board
import busio
import adafruit_vcnl4010
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_vcnl4010.VCNL4010(i2c)

print('Proximity: {0}'.format(sensor.proximity))
print('Ambient light: {0} lux'.format(sensor.ambient_lux))
