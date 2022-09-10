print("Welcome To My Python Calculator")
firstNumber = input("Enter First Number :")
print("+, -, *, /, %  :")
operator = input("Enter any one of above function")
secondNumber = input("Enter Second Number :")

if operator == "+" :
    print(int(firstNumber) + int(secondNumber))

elif operator == "-" :
    print(int(firstNumber) - int(secondNumber))

elif operator == "/" :
    print(int(firstNumber) / int(secondNumber))

elif operator == "%" :
    print(int(firstNumber) % int(secondNumber))

else :
    print("Invalid operator selected")
