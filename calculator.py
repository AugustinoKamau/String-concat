# calculator

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