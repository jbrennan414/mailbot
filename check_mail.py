import datetime
import time
import board
import digitalio
import adafruit_lis3dh

from tinydb import TinyDB, Query
db = TinyDB('db.json')

def did_text_today():
  Record = Query()
  today = datetime.date.today().strftime("%Y-%m-%d")
  f = db.search(Record.date == today)
  if not f:
    return False
  return True

print(did_text_today())

# Every minute

# Check for mail (laser)



# Is flag raised?
i2c = board.I2C()
int1 = digitalio.DigitalInOut(board.D6)
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, int1=int1)

x,y,z = lis3dh.acceleration
print(x,y,z)

# Check to see if we've texted Cole today

# Call rest api

# If 200, add to tinydb

 
