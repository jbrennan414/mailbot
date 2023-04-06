import datetime
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

# Check to see if we've texted Cole today

# Call rest api

# If 200, add to tinydb

 
