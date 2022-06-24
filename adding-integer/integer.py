

name = input("what is your name? \n")
allowedUsers = ["seyi", "mike", "love"]
allowedPassword = ["passwordSeyi" , "passwordMike" , "passwordLove"]


if(name in allowedUsers):
    password = input("your password? \n")
    userId = allowedUsers.index(name)

    if(password == allowedPassword[userId]):
        print("welcome %s" % name)
        
    else:
        print("password incorrect, please try again")

else:
    print("name not found,please try again")
