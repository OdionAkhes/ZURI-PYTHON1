# initializing system
import random

database = {}  # dictionary


def init():

    isValidOptionSelected = False
    print("Welcome to bank PHP")

    while isValidOptionSelected == False:

        haveAccount = int(input("Do you have an account with us: 1 (yes) 2 (no) \n"))

        if(haveAccount == 1):
            isValidOptionSelected = True
            login()
        elif(haveAccount == 2):
            isValidOptionSelected == True
            register()
        else:
            print("you have selected invalid option")


def login():
    print("Login to your account")
    
    isLoginSuccessful = False
    
    while isLoginSuccessful == False:
        
        accountNumberFromUser = int(input("What is yur account number? \n"))
        password = input("What is your password \n")
        
        for accountNumber,userDetails in database.items():
            if(accountNumber == accountNumberFromUser):
                if(userDetails[3] == password):
                    isLoginSuccessful = True
                    
        print("Invalid account or password")    
    bankOperation(userDetails)
    
def register():

    print("register")
    
    email = input("What is your email address? \n")
    firstName = input("What is your first name? \n")
    lastName = input("What is your last name? \n")
    password = input("create a password for yourself \n")

    accountNumber = generationAccountNumber()
    database[accountNumber] = [firstName, lastName, email, password]
    
    print("Your Account has been created")
    print(" == ==== ===== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print(" == ==== ===== ===== ===")
    
    login()



def bankOperation(user):
    print("Welcome %s %s" % ( user[0], user[1]))
    
  
    

        
    selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit"))
        
    if(selectedOption == 1):
    
        depositOperation()
    elif(selectedOption == 2):
    
        withdrawalOperation()
    elif(selectedOption == 3):
        
        login()
    elif(selectedOption == 4):
        
        exit()
    else: 

        print("Invalid option selected")
        bankOperation(user)
    
        
def withdrawalOperation():
    print("withdrawal")
    
def depositOperation():
    print("Deposit Operations")
    
def generationAccountNumber():
    return random.randrange(1111111111, 9999999999)


print(generationAccountNumber())

init()