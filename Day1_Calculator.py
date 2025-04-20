"""Day 1 of 100 days pyhton mini projects 
Build a menu driven calculator using python capable of performing:
1. Addition a+b
2. Subtraction a-b
3. Multiplication a*b
4. Division a/b
5. Modulus a%b
6. Exponentiation a**b 
Mohammad Iqbal Hurrah 
Date: 19-April-2025
Day: "Saturday" """
print("""Author: "Mohammad Iqbal Hurrah"
Date:  "19-April-2025" """)
def data():
    global num1, num2
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
def expo(a,b):
    return a**b
def terminate():
    print("Terminating the program..!")
    import sys
    sys.exit()
data()
while True:
    print("""||  +++++++++++++++++++++++++++++++++++++++++++ || Press || +++++++++++++++++++++++++++++++++++++  ||
          + for addition
          - for subtraction
          * for multiplication
          / for division
          % for modulus
          ^ for exponentiation
          ! for terminating the program 
          0 for entering new data """)
    choice = input("Enter your choice here: ")
    if choice == "+":
        result = addition(num1,num2)
        print(f"Addition of {num1} and {num2} = ", result)
    elif choice == "-":
        result = subtraction(num1,num2)
        print(f"Difference of {num1} and {num2} = ", result)
    elif choice == "*":
        result = multiplication(num1,num2)
        print(f"Product of {num1} and {num2} = ", result)
    elif choice == "/":
        if num2 == 0:
            print("Error: Not Defined")
        else:
            result = div(num1,num2)
            print(f"Result of {num1} divide by {num2} = ", result)
    elif choice == "%":
        if num2 == 0:
            print("Error: Not Defined")
        else:
            result = mod(num1,num2)
            print(f"Result of {num1} modulus {num2} = ", result)
    elif choice == "^":
        result = expo(num1,num2)
        print(f"Result of {num1} power {num2} = ", result)
    elif choice == "0":
        data()
    elif choice == "!":
        terminate()
    else:
        print("Wrong input..!")