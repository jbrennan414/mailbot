from datetime import datetime
import time
import board
import busio
import digitalio
import adafruit_lis3dh
import adafruit_vcnl4010
import json
import os
import webbrowser
import requests

from tinydb import TinyDB, Query
db = TinyDB('db.json')
now = datetime.now()

def did_text_today():
  Record = Query()
  today = now.strftime("%Y-%m-%d")
  f = db.search(Record.date == today)
  if not f:
    return False
  return True

def check_for_mail():
  i2c = busio.I2C(board.SCL, board.SDA)
  sensor = adafruit_vcnl4010.VCNL4010(i2c)
  mailboxDepth = 3000 # We will change this later
  proximity = int(format(sensor.proximity))

  if proximity > mailboxDepth:
    print("we have mail")
  else:
    print("we dont have mail")

  print('Proximity: {0}'.format(sensor.proximity))
  print('Ambient light: {0} lux'.format(sensor.ambient_lux))

def is_flag_raised():
  i2c = board.I2C()
  int1 = digitalio.DigitalInOut(board.D6)
  lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, int1=int1)

  x,y,z = lis3dh.acceleration
  print(x,y,z)

def send_text():
  api_url = "https://0v17ybsk9g.execute-api.us-west-2.amazonaws.com/prod/mailbot"
  response = requests.get(api_url)
  json_response = json.loads(response.text)
  statusCode = json_response["statusCode"]
  if statusCode == 200:
    today = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M")
    db.insert({'date':today, 'time':current_time})


# Every minute

# Check for mail (laser)
check_for_mail()

# Is flag raised?
is_flag_raised()

# Check to see if we've texted Cole today
did_text_today()

# Call rest api
send_text()


# If 200, add to tinydb
print(db.all())
