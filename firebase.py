import pyrebase


firebaseConfig = {

  "apiKey": "AIzaSyBLlxUWh5IdHF6fgRvAWl36uchOe96vbx0",

  "authDomain": "flet-test-3465b.firebaseapp.com",

  "projectId": "flet-test-3465b",

  "databaseURL": "https://flet-test-3465b-default-rtdb.firebaseio.com",


  "storageBucket": "flet-test-3465b.appspot.com",

  "messagingSenderId": "244360038277",

  "appId": "1:244360038277:web:c331d6ecda60670568a6ec"

}


firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()



def stream_handler(message):
    print(message["event"]) # put
    print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}

my_stream = db.child("counter").stream(stream_handler)