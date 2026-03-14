import os
import time
import pyrebase
from dotenv import load_dotenv

load_dotenv()

firebaseConfig = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "projectId": os.getenv("FIREBASE_PROJECT_ID"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
    "appId": os.getenv("FIREBASE_APP_ID"),
    "databaseURL": ""
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

print("=" * 30)
print("      aLfabe Mail")
print("=" * 30)

def dogrulama():
    while True:
        print("Please enter your email:")
        email = input()
        try:
            auth.sign_in_with_email_and_password(email, "wrongpassword123!")
        except Exception as e:
            if "INVALID_PASSWORD" in str(e) or "INVALID_LOGIN_CREDENTIALS" in str(e):
                print("Your email is correct!")
                return email
            elif "EMAIL_NOT_FOUND" in str(e) or "INVALID_EMAIL" in str(e):
                print("Your email is incorrect, please try again.")
            else:
                print("Your email is incorrect, please try again.")

def dogrulama2(email):
    for deneme in range(3):
        kalan = 3 - deneme
        print(f"Remaining attempts: {kalan}")
        print("Please enter your password:")
        password = input()
        try:
            auth.sign_in_with_email_and_password(email, password)
            print("Your password is correct!")
            return True
        except:
            print("Your password is incorrect!")

    print("Your account is locked! Please try again after 3 minutes.")
    time.sleep(180)
    return False

def kayit_ol():
    print("Please enter your email:")
    email = input()
    print("Please enter your password:")
    password = input()
    try:
        auth.create_user_with_email_and_password(email, password)
        print("Sign up successful! Welcome to aLfabe Mail!")
    except:
        print("This email is already registered or password is too short!")

def sifremi_unuttum():
    print("Please enter your email:")
    email = input()
    try:
        auth.send_password_reset_email(email)
        print("Password reset email sent! Please check your inbox.")
    except:
        print("Email not found!")

while True:
    print("\n1 - Sign Up")
    print("2 - Sign In")
    print("3 - Forgot Password")
    print("4 - Exit")
    secim = input("Selection: ")

    if secim == "1":
        kayit_ol()
    elif secim == "2":
        email = dogrulama()
        if email != False:
            result = dogrulama2(email)
            if result == True:
                print("Welcome to aLfabe Mail!")
    elif secim == "3":
        sifremi_unuttum()
    elif secim == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid selection!")