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


    # This part of the program will be asking users to complete a transaction through the ATM
    print("Please insert your ATM card\n")
    print("Welcome to Cash-R-Us ATM",first_name,last_name,"\n")
    userPIN = input("What is your 4 digit PIN: ")

    if pin == userPIN:
        balance = 674
        print("\n Your Balance: $" + str(balance))

        # Ask users what type of transaction they want - Withdrawal - Deposit
        typeofTransaction = input("\nWould you like to make a Withdrawal, Deposit, or check your Balance\nW = Withdrawal - D = Deposit - B = Balance: ").lower()
        if typeofTransaction == "w":
            withdAmount = int(input("Enter amount of money you want to withdrawal: "))


            if withdAmount > balance:
                print("Sorry but you don't have that enough money in your account to withdrawal that money.")

            else:
                balance = balance - withdAmount
                print("Your new balance is: $" + str(balance))
        
        elif typeofTransaction == "d":
            depoAmount = int(input("Enter amount of money you want to deposit: "))
            balance = balance + depoAmount
            print("Your new balance is: $" + str(balance))

        else:
            print("Your current balance is: $" + str(balance))
            
        
    else:
        print("\nSorry",first_name,last_name,"the PIN you entered was incorrect")




else:
    print("\n Have a nice day",first_name,last_name + ", please come back and visit soon." )

