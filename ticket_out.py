import json
from pprint import pprint

 


departureTime_hour = ""
departureTime_minute = ""
flightNumber = ""
aircraftType = ""
destination = ""
flightStatus = ""
baseCost = ""
durationInMinutes = ""
fl = "lo"
new_val = ""


 



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
            departureTime_hour = str(json.dumps((x["departureTime"]["hour"])))
            departureTime_minute = str(json.dumps((x["departureTime"]["minute"])))

            
            
            


                   

                          
           

                          

            

            #sql = "INSERT INTO flight_data (id, flight_number, aircraft_type, destination, flight_status, base_cost, duration_minutes, departuretime_hour, departuretime_minute, departuretime_minute) VALUES ('', flightNumber, aircraftType, destination, flightStatus, baseCost, durationInMinutes, departureTime_hour, departureTime_minute)"
            #mycursor.execute(sql)
            #mydb.commit()
            #print(mycursor.rowcount, "record inserted.")
            #print(x["destination"])
  
                #departureTime_minute.append(y["minute"])
                #print()






        
#pprint(flightNumber)
#pprint(aircraftType)
#pprint(destination)
#pprint(flightStatus)
#pprint(baseCost)
#pprint(durationInMinutes)
