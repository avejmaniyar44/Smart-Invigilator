import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyBstGfA-Rkh-4MrE2_tIIBObCsaj81pCNI",
    "authDomain": "examplatform-329f9.firebaseapp.com",
    "databaseURL": "https://examplatform-329f9-default-rtdb.firebaseio.com",
    "projectId": "examplatform-329f9",
    "storageBucket": "examplatform-329f9.appspot.com",
    "messagingSenderId": "337104311096",
    "appId": "1:337104311096:web:1716a4bffe287c29d567cd",
    "measurementId": "G-468QDB02B2"
  }

firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()