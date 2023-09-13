import firebase_admin
from firebase_admin import credentials, auth


cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)

email = input("enter Email:")
password = input("enter password:")
phone = input('enter phone:')
id = input("enter ID:")

user = auth.create_user(uid=id, email=email, password=password, phone_number=phone)
print(f"user created {user.uid}")