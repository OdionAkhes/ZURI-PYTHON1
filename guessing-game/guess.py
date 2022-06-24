# ourFaveNumber = 10

# userGuess = input("enter your guess: ")

# print(type(userGuess))

# userGuess = int(userGuess)

# print(type(userGuess))

# if userGuess == ourFaveNumber:
#     print("success,you guessed the number! our favorite number is:" +
#           str(ourFaveNumber))

# if userGuess < ourFaveNumber:
#     print("your guess is too low. try a little higher")

# if userGuess > ourFaveNumber:
#     print("your guess is too high. try a little lower")


from re import U


# userNo = input("enter a number: ")

# try:
#     userNo = int(userNo)
#     print("hooray,you entered a number ")

#     if userNo >= 0:t
#         print("true")
#     else:
#         print("false")
# except:
#     print("this is not a number")
userSentence = input("enter a sentence: ")

userSentence = userSentence.strip(" ")

listOfWords = userSentence.split(" ")

noOfWords = len(listOfWords)

print(noOfWords)
