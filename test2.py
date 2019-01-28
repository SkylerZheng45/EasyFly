import json
from pprint import pprint
import pyrebase
import pandas as pd
from auth import *


config = {
  "apiKey": "AIzaSyD-Fy3mSos_QBShFXgrqGNp_Vh78UUR-ew",
  "authDomain": "easyfly-3cc98.firebaseapp.com",
  "databaseURL": "https://easyfly-3cc98.firebaseio.com",
  "storageBucket": "easyfly-3cc98.appspot.com",
   "messagingSenderId": "135959500080",
  "serviceAccount": "/Users/abinavc/AA-Mock-Engine/mock/easyfly-3cc98-22c0cda76e05.json",

}
firebase = pyrebase.initialize_app(config)

need_fill = []

db = firebase.database()






# add do a variable

to = db.child("to").get().val()

   


code = ""
state_code = ""
city = ""
country_code = ""
country_name = ""
latitude = ""
longitude = ""
destination_city = to
airports = []
tickets = []
 



with open('/Users/abinavc/AA-Mock-Engine/mock/airports.json') as f:
    data = json.load(f)

    for x in data:
        city = str(json.dumps((x["city"])))
        code = str(json.dumps((x["code"])))
        state_code = str(json.dumps((x["stateCode"])))
        country_code = str(json.dumps((x["countryCode"])))
        country_name = str(json.dumps((x["countryName"])))
        latitude = str(json.dumps((x["latitude"])))
        longitude = str(json.dumps((x["longitude"])))
        text = city.strip()
        if str(x["city"]) == destination_city:
            airports.append(str(x["code"]))

    
    		#sql = "INSERT INTO flight_data (id, flight_number, aircraft_type, destination, flight_status, base_cost, duration_minutes, departuretime_hour, departuretime_minute, departuretime_minute) VALUES ('', flightNumber, aircraftType, destination, flightStatus, baseCost, durationInMinutes, departureTime_hour, departureTime_minute)"
    		#mycursor.execute(sql)
    		#mydb.commit()
    		#print(mycursor.rowcount, "record inserted.")
    		#print(x["destination"])
  
    			#departureTime_minute.append(y["minute"])
    			#print()

with open('/Users/abinavc/AA-Mock-Engine/mock/flightData.json') as f:
    data = json.load(f)

    for i in data.values():

        for x in i["flights"]:

            flightNumber = str(json.dumps((x["flightNumber"])))
            aircraftType = str(json.dumps((x["aircraftType"])))
            destination = str(json.dumps((x["destination"])))
            flightStatus = str(json.dumps((x["flightStatus"])))
            baseCost = str(json.dumps((x["baseCost"])))
            durationInMinutes = str(json.dumps((x["durationInMinutes"])))
            epartureTime_hour = str(json.dumps((x["departureTime"]["hour"])))
            departureTime_minute = str(json.dumps((x["departureTime"]["minute"])))

            for i in airports:
                if i == str(x["destination"]):
                    tickets.append("Flight Number: " + x["flightNumber"] + " Aircraft Type: " + x["aircraftType"]+ " " + " Destination: " +x["destination"]+ " FlightStatus: " + x["flightStatus"])


destination.child('ticketInfo11').push(str(x["flightNumber"]))
db.child('ticketInfo12').push(str(x["destination"]))

print(tickets)




    	
#pprint(flightNumber)
#pprint(aircraftType)
#pprint(destination)
#pprint(flightStatus)
#pprint(baseCost)
#pprint(durationInMinutes)
