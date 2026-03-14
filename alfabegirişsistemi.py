import time

print("aLfabe Mail")
personaccount = "user1"
personpassword = "123456"
print("Please enter your Account")
userid = input()

def dogrulama():
    if userid == personaccount:
        print("Your id is correct")
        return True
    else:
        print("Your id is false or blocked please try again after 3 minutes.")
        time.sleep(180)
        return False

dogrulama()

def dogrulama2():
        print("Please enter your password")
        userpassword = input()
        if userpassword == personpassword:
            print("Your password is correct")
            return True
        else:
            print("Your password is false or blocked please try again after 3 minutes.")
            time.sleep(180)
            return False
if dogrulama() == True:
    dogrulama2()
print("Welcome to aLfabe Mail")
