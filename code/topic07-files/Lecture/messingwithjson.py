# Messing with JSON
# This is program is to demonstrate 
# storing data in a json format
#
# Author: Andrew Beatty


import json


electricBill = {
    'name' : 'Andrew',
    'amount' : '99999'
}

with open("storeData.json", "wt") as f:
    json.dump(electricBill, f) # writes the dictionary object to the file as a JSON object

