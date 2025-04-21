"""Temperature Converter capable of following features:
1.C to F    # (C*9/5)+32
2. F to C   # (F-32)*5/9
3. C to K   # (C+273.15)
4. K to C   # (K-273.15)
5. F to K   # (F-32)*5/9+273.15
6. K to F   # (K-273.15)*9/5+32"""
print("""    Author: "Mohammad Iqbal Hurrah"
    Date: 21-April-2025
        \n************************************* || Temperature Converter || **********************************""")
def show():
    print("""   1. Celsius to Fahrenheit.
    2. Fahrenheit to Celsius.
    3. Celsius to Kelvin.
    4. Kelvin to Celsius.
    5. Fahrenheit to Kelvin.
    6. Kelvin to Fahrenheit.
    7. Terminate the program. """)
def c_to_f(celsius):
    fahrenheit = (celsius*9/5)+32 
    return fahrenheit
def f_to_c(fahrenheit):
    celsius = (fahrenheit-32)*5/9
    return celsius
def c_to_k(celsius):
    kelvin = (celsius+273.15)
    return kelvin
def k_to_c(kelvin):
    celsius = (kelvin-273.15)
    return celsius
def f_to_k(fahrenheit):
    kelvin = (fahrenheit-32)*5/9+273.15
    return kelvin
def k_to_f(kelvin):
    fahrenheit = (kelvin-273.15)*9/5+32
    return fahrenheit

def terminate():
    import sys 
    sys.exit()
    return "Program Terminated Successfully...!"
while True:
    temp = float(input("Enter Temperature: "))
    show()
    choice = input("Enter your choice: ")
    if choice == "1":
        result = c_to_f(temp)
        print("Temperature in Fahrenheit is ", result)
    elif choice == "2":
        result = f_to_c(temp)
        print("Temperature in Celsius is ", result)
    elif choice == "3":
        result = c_to_k(temp)
        print("Temperature in kelvin is ",result)
    elif choice == "4":
        result = k_to_c(temp)
        print("Temperature in celsius is ", result)
    elif choice == "5":
        result = f_to_k(temp)
        print("Temperatuere in kelvin is ", result)
    elif choice == "6":
        result = k_to_f(temp)
        print("Temperatuere in Fahrenheit is ", result)
    elif choice == "7":
        print("Program Terminated Successfully...!")
        terminate()
    else:
        print("Wrong Choice. Please Enter a Valid Choice: ")