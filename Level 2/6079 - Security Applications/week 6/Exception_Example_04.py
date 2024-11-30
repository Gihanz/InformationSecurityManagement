import random
import datetime


# Variables  ------------------------------------------------
datTodayTime = datetime.datetime.now()
datToday = datetime.datetime.now().date()
strBreak = "-" * 25

import json

user_json = '{"name": "John", "age": 39}'
user = json.loads(user_json)

try:
    print(user['name'])
    print(user['age'])
    print(user['address'])
    ...
except KeyError as e:
    print("There are missing fields in the user object: ", e)
    # Properly handle the error
