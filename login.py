from datetime import datetime
import time
import sys

email = "mdavalos392@gmail.com"
password = "123456789"

def valid_Email(str):
    if str == email:
        print("Email is valid")
        print()
    else:
        print("Email entered was invaid please try again.")
        secondTryEmail = input("Email: ")
        valid_Email(secondTryEmail)

def forgot_Password():
    newPassword = input("Please type in your new Password: ")
    password = newPassword
    print("Your new password is: " + password)

def valid_Password (str):
    if(str == password):
        print("Password is Valid")
        print()
    else:
        print("Sorry you have entered an invalid Password. Try again or select Forgot Password. ")
        selection = input("Select 1 for Forgot password or 2 to try again: ")
        if selection == "1":
            forgot_Password()
            return
        else:
            print("Please try Password again: ")
            secondTryPass = input("Password: ")
            valid_Password(secondTryPass)
    

def email_Verification():
    print("Please check your email for a verication. Wait for 2 seconds. ")
    time.sleep(2.5)
    now = datetime.now()
    dt_string = now.strftime("%m/%d/%Y at %H:%M:%S")
    print("We have noticed that someone is trying to login using your account on " + dt_string + ". Is this you")
    verify = input("Enter Y for yes or N for no: ")
    if verify == "Y" or verify == "y":
        print("Login Successfully!!")
    else:
        print("Thank you for letting us know. ")

loop = True
while(loop):    
    x = input("Welcome to my Web Page. Please login with your email and password. Press enter to continue or type 'Q' to quit: ")
    if x == "Q" or x == "q":
        print("See you later!")
        sys.exit(1)
    userEmail = input("Email: ")
    valid_Email(userEmail)
    userPassword = input("Password: ")
    valid_Password(userPassword)
    email_Verification()