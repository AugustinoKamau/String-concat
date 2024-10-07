# calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

user = input("Enter Operation (+,-,*,/): ")

if user == "+":
    result = num1 + num2
    print("The sum is", result)

elif user == "-":
    result = num1 - num2
    print("The difference is", result)

elif user == "*":
    result = num1 * num2
    print("The product is", result)