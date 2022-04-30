import pyrebase

config = {
    "apiKey": "AIzaSyBR_HchrcuS-pxD0tPkva0jpAgW6zX_yNY",
    "authDomain": "dragonhack2022.firebaseapp.com",
    "databaseURL": "https://dragonhack2022-default-rtdb.firebaseio.com",
    "projectId": "dragonhack2022",
    "storageBucket": "dragonhack2022.appspot.com",
    "messagingSenderId": "696007826227",
    "appId": "1:696007826227:web:a0c6ed99971cfc7349fc46",
    "measurementId": "G-YRDW7VJEZJ"
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()

data = {"email": "test@gmail.com", "city": "Philadelphia", "subscribe": True}

database.push(data)