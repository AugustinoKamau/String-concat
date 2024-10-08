# calculator

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y !=0:
        return x / y
    
    else:
        return "Error the it is not divisible by 0."
    
while True:



    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    user = input("Enter Operation (+,-,*,/): ")

    #Calculating the operation.

    #Addition.
    if user == "+":
        result = num1 + num2
        print("The sum is", result)

    #Substraction.
    elif user == "-":
        result = num1 - num2
        print("The difference is", result)
    
    #Multiplication.
    elif user == "*":
        result = num1 * num2
        print("The product is", result)
    
    #Division
    elif user =="/":
        #Check that the second number input is not divisible by 0.
        if num2 != 0:
            result = num1 / num2
            print("The product is", result)
    
        else:
            print("Error: num1 is not divisible by 0")
    
    else:
        print("Invalid entry.")