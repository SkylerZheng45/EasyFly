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

db = firebase.database()
result = db.child("numOfPassengers").get()



# add do a variable


#and now the hard/ easy part that took me a while to figure out:
# notice the value inside the .child, it should be the parent name with all the cats keys
values = db.child('numOfPassengers').get()

# adding all to a dataframe you'll need to use the .val()  
data = pd.DataFrame(values.val())

print(data.head())