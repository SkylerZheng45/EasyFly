import pyrebase
config = {
  "apiKey": "AIzaSyA3h_DzfjgPTbQXcvyVlhMZe7qziDFpRpc",
  "authDomain": "easyfly-8136e.firebaseapp.com",
  "databaseURL": "https://databaseName.firebaseio.com",
  "storageBucket": "easyfly-8136e.appspot.com",
  "serviceAccount": "/Users/abinavc/Downloads/easyfly-8136e-firebase-adminsdk-idzuy-a42ce7b57b.json"
}
firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
#authenticate a user
user = auth.sign_in_with_email_and_password("william@hackbrightacademy.com", "mySuperStrongPassword")