
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def modulus(a,b):
    return a%b

n1 = float(input("Enter First Number: "))
n2 = float(input("Enter Second Number: "))
print("Operations: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")

choice = input("Select Operation: ")
if choice == "1":
    print(n1, "+", n2, "=", add(n1,n2))
elif choice == "2" :
    print(n1, "-", n2, "=", subtract(n1,n2))
elif choice == "3" :
    print(n1, "*", n2, "=", multiply(n1,n2))
elif choice == "4" :
    print(n1, "/", n2, "=", divide(n1,n2))
elif choice == "5" :
    print(n1, "%", n2, "=", modulus(n1,n2))
else:
    print("Invalid Operation")



