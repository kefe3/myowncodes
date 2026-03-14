import os
import re
import time
import pyrebase
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

firebaseConfig = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "projectId": os.getenv("FIREBASE_PROJECT_ID"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
    "appId": os.getenv("FIREBASE_APP_ID"),
    "databaseURL": "https://alfabe-7508c-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

print("=" * 30)
print("      aLfabe Mail")
print("=" * 30)

# ── YARDIMCI ──
def email_key(email):
    return email.replace(".", "_").replace("@", "_at_")

# ── AUTH ──

def dogrulama():
    while True:
        print("Please enter your email:")
        email = input().strip()
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            print("Your email is incorrect, please try again.")
            continue
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
            user = auth.sign_in_with_email_and_password(email, password)
            print("Your password is correct!")
            return user
        except:
            print("Your password is incorrect!")
    print("Your account is locked! Please try again after 3 minutes.")
    time.sleep(180)
    return False

def kayit_ol():
    print("Please enter your email:")
    email = input().strip()
    print("Please enter your password:")
    print("(At least 8 characters, 1 uppercase letter, 1 number)")
    password = input()
    if len(password) < 8 or not any(c.isupper() for c in password) or not any(c.isdigit() for c in password):
        print("Password is too weak! Please follow the rules.")
        return
    print("Please enter your password again:")
    password2 = input()
    if password != password2:
        print("Passwords do not match!")
        return
    try:
        auth.create_user_with_email_and_password(email, password)
        print("Sign up successful! Welcome to aLfabe Mail!")
    except:
        print("This email is already registered or password is too short!")

def sifremi_unuttum():
    print("Please enter your email:")
    email = input().strip()
    try:
        auth.send_password_reset_email(email)
        print("Password reset email sent! Please check your inbox.")
    except:
        print("Email not found!")

# ── MAIL ──

def mail_gonder(user, email):
    print("To:")
    to = input().strip()
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', to):
        print("Invalid email address!")
        return
    print("Subject:")
    subject = input().strip()
    print("Message:")
    body = input().strip()

    mail = {
        "from": email,
        "to": to,
        "subject": subject,
        "body": body,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "deleted": False
    }

    db.child("mails").child(email_key(to)).child("inbox").push(mail, user["idToken"])
    print("Mail sent successfully!")

def gelen_kutusu(user, email):
    print("\n=== Inbox ===")
    data = db.child("mails").child(email_key(email)).child("inbox").get(user["idToken"])

    mail_list = []
    if data.val():
        for key, val in data.val().items():
            if not val.get("deleted", False):
                mail_list.append((key, val))

    if not mail_list:
        print("Your inbox is empty!")
        return

    for i, (key, val) in enumerate(mail_list):
        print(f"{i+1}. From: {val['from']} | Subject: {val['subject']} | {val['time']}")

    print("\nEnter mail number to read (or 0 to go back):")
    secim = input().strip()
    if secim == "0":
        return
    try:
        idx = int(secim) - 1
        key, val = mail_list[idx]
        print(f"\nFrom: {val['from']}")
        print(f"Subject: {val['subject']}")
        print(f"Time: {val['time']}")
        print(f"Message: {val['body']}")
    except:
        print("Invalid selection!")

def mail_sil(user, email):
    print("\n=== Delete Mail ===")
    data = db.child("mails").child(email_key(email)).child("inbox").get(user["idToken"])

    mail_list = []
    if data.val():
        for key, val in data.val().items():
            if not val.get("deleted", False):
                mail_list.append((key, val))

    if not mail_list:
        print("Your inbox is empty!")
        return

    for i, (key, val) in enumerate(mail_list):
        print(f"{i+1}. From: {val['from']} | Subject: {val['subject']}")

    print("\nEnter mail number to delete (or 0 to go back):")
    secim = input().strip()
    if secim == "0":
        return
    try:
        idx = int(secim) - 1
        key, _ = mail_list[idx]
        db.child("mails").child(email_key(email)).child("inbox").child(key).update({"deleted": True}, user["idToken"])
        print("Mail deleted!")
    except:
        print("Invalid selection!")

def taslak_kaydet(user, email):
    print("To:")
    to = input().strip()
    print("Subject:")
    subject = input().strip()
    print("Message:")
    body = input().strip()

    draft = {
        "from": email,
        "to": to,
        "subject": subject,
        "body": body,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    db.child("mails").child(email_key(email)).child("drafts").push(draft, user["idToken"])
    print("Draft saved!")

def taslak_goster(user, email):
    print("\n=== Drafts ===")
    data = db.child("mails").child(email_key(email)).child("drafts").get(user["idToken"])

    draft_list = []
    if data.val():
        for key, val in data.val().items():
            draft_list.append((key, val))

    if not draft_list:
        print("No drafts found!")
        return

    for i, (key, val) in enumerate(draft_list):
        print(f"{i+1}. To: {val['to']} | Subject: {val['subject']} | {val['time']}")

    print("\nEnter draft number to view (or 0 to go back):")
    secim = input().strip()
    if secim == "0":
        return
    try:
        idx = int(secim) - 1
        key, val = draft_list[idx]
        print(f"\nTo: {val['to']}")
        print(f"Subject: {val['subject']}")
        print(f"Message: {val['body']}")

        print("\n1 - Send this draft")
        print("2 - Delete this draft")
        print("3 - Go back")
        alt_secim = input("Selection: ").strip()
        if alt_secim == "1":
            if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', val['to']):
                print("Invalid recipient email!")
                return
            mail = {**val, "deleted": False}
            db.child("mails").child(email_key(val['to'])).child("inbox").push(mail, user["idToken"])
            db.child("mails").child(email_key(email)).child("drafts").child(key).remove(user["idToken"])
            print("Draft sent!")
        elif alt_secim == "2":
            db.child("mails").child(email_key(email)).child("drafts").child(key).remove(user["idToken"])
            print("Draft deleted!")
    except:
        print("Invalid selection!")

# ── MAIL MENÜSÜ ──

def mail_menu(user, email):
    while True:
        print(f"\nWelcome, {email}!")
        print("1 - Inbox")
        print("2 - Send Mail")
        print("3 - Save Draft")
        print("4 - Drafts")
        print("5 - Delete Mail")
        print("6 - Sign Out")
        secim = input("Selection: ").strip()

        if secim == "1":
            gelen_kutusu(user, email)
        elif secim == "2":
            mail_gonder(user, email)
        elif secim == "3":
            taslak_kaydet(user, email)
        elif secim == "4":
            taslak_goster(user, email)
        elif secim == "5":
            mail_sil(user, email)
        elif secim == "6":
            print("Signed out!")
            break
        else:
            print("Invalid selection!")

# ── ANA MENÜ ──

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
        if email:
            user = dogrulama2(email)
            if user:
                mail_menu(user, email)
    elif secim == "3":
        sifremi_unuttum()
    elif secim == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid selection!")