import json
from pprint import pprint
import mysql.connector

departureTime_hour = []
departureTime_minute = []
flightNumber = []
aircraftType = []
destination = []
flightStatus = []
baseCost = []
durationInMinutes = []



with open('/Users/abinavc/AA-Mock-Engine/mock/flightData.json') as f:
    data = json.load(f)

    for i in data.values():

    	for x in i["flights"]:

    		flightNumber.append(x["flightNumber"])
    		aircraftType.append(x["aircraftType"])
    		destination.append(x["destination"])
    		flightStatus.append(x["flightStatus"])
    		baseCost.append(x["baseCost"])
    		durationInMinutes.append(x["durationInMinutes"])
    		departureTime_hour.append(x["departureTime"]["hour"])
    		departureTime_minute.append(x["departureTime"]["minute"])

    		#print(x["destination"])
  
    			#departureTime_minute.append(y["minute"])
    			#print()





    	
#pprint(flightNumber)
#pprint(aircraftType)
#pprint(destination)
#pprint(flightStatus)
#pprint(baseCost)
#pprint(durationInMinutes)
