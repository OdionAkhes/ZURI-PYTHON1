# simple cli calculator

print("welcome to simple CLI Calculator")

itsRunning = True

while itsRunning:
    # processing calculations

    print("starting calculator process")
    userOperation = input(
        "what operation would you like to perform?\nPick any of ['+','-','*','/'] : ")

    # get user numbers
    try:  # try to get user numbers, if theyre valid integers/floats,continue
        no1 = float(input("first number: "))
        no2 = float(input("second number: "))

    except:  # we get an error when running it
        print("failed,invalid numbers...")
        continue

    if userOperation == "+":
        print(no1 + no2)
        # perform addition
    elif userOperation == "-":
        print(no1 - no2)
        # perform subtraction
    elif userOperation == "*":
        print(no1 * no2)
        # perform multiplication
    elif userOperation == "/":
        print(no1 / no2)
        # perform division

    else:
        # invalid operation
        print("invalid operation entered, try again")

    choice = input("would you like to run another calculation. [y,n]")
    if choice == "y":
        pass
    if choice == "n":
        itsRunning = False
   # THIS IS A BREAK
