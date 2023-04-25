from dotenv import load_dotenv
load_dotenv()
from datetime import datetime
import sched, time
import board
import busio
import digitalio
import adafruit_lis3dh
import json
import os
import webbrowser
import requests
import adafruit_vl53l4cd

from tinydb import TinyDB, Query
db = TinyDB('db.json')
now = datetime.now()


def did_text_today():
  Record = Query()
  today = now.strftime("%Y-%m-%d")
  f = db.search(Record.date == today)
  if not f:
    print("We did not text today")
    return True
  print("We have texted today")
  return False

def check_for_mail():
  i2c = board.I2C()
  vl53 = adafruit_vl53l4cd.VL53L4CD(i2c)
  vl53.start_ranging()

  mailboxDepth = 13 # we will change this later

  while not vl53.data_ready:
    pass
  vl53.clear_interrupt()

  if mailboxDepth > vl53.distance:
    print("you've got mail")
    return True
  else:
    print("no mail yet")
    return False

def is_flag_raised():
  i2c = board.I2C()
  int1 = digitalio.DigitalInOut(board.D6)
  lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, int1=int1)

  x,y,z = lis3dh.acceleration

  flag_fudge_factor = 4

  if abs(x) < flag_fudge_factor:
    return True
  else:
    return False

def send_text():
  api_url = "https://0v17ybsk9g.execute-api.us-west-2.amazonaws.com/prod/mailbot"
  headers = {'x-api-key': os.environ.get("API_KEY")} # I won't need to send this to Cole if I mail him the pi
  response = requests.get(api_url, headers=headers)
  json_response = json.loads(response.text)
  print(json_response)
  statusCode = json_response["statusCode"]
  if statusCode == 200:
    today = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M")
    db.insert({'date':today, 'time':current_time})


def do_something(scheduler): 
    # schedule the next call first
    scheduler.enter(60, 1, do_something, (scheduler,))
    if all([check_for_mail(), did_text_today(), is_flag_raised()]):
      print("all systems GOOOOO")
      send_text()
    else: 
      print("all systems NOOOOO")


my_scheduler = sched.scheduler(time.time, time.sleep)
my_scheduler.enter(60, 1, do_something, (my_scheduler,))
my_scheduler.run()
