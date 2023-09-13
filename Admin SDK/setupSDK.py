import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("key.json")
app = firebase_admin.initialize_app(cred)
print(app)