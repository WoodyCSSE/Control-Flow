# Developer: Woody Tilbury
#Date: 10/11/2021
#Program: ATM Bank Transaction

'''
This program simulates an ATM utilizing IF, ELIF, and ELSE statements
Nesting our IF statements and refresh our comparison and logical operators
'''

print("Welcome to Cash-R-Us Bank\n\nLet's take a moment to set up your account.\n")

# Set up account by asking users their first and last names using Variables
first_name = input("What is your first name: ")
last_name = input("What is your last name: ")
print("\nWelcome to Cash-R-Us",first_name,last_name + ", we will now set up a security PIN on your account\n")

# Set up a PIN - Personal Identification Number
pin = input("Choose a 4-digit PIN: ")
print("\nThank you",first_name + ",we see that you set your PIN to",pin)

print("\nWould you like to make a transaction through our Automated Teller Machine")
atm = input("Yes or No: ").lower()

if atm == "yes":
    print("\n *******************************************************************************************\n")



else:
    print("\n Have a nice day",first_name,last_name + ", please come back and visit soon." )