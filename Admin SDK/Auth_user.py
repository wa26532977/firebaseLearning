import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)

email = input("enter email:")
user = auth.get_user_by_email(email)

print(f"user id {user.uid}, user phone: {user.phone_number}")