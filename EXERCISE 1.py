print("Amigos! I am pratcing python programming")


num1 = float(input("Enter first number: "))
num2 = float(input("Enter Second number: "))

ope = input("Enter the operator: ")
if ope == "+":
    result = num1 + num2 
elif ope == "-":
    result = num1 - num2
elif ope == "*":
    result = num1 * num2
if ope == "/":
    if num2 == 0:
        print("Zero can't divide")
    else:
        result = num1 / num2 
elif ope == "%":
    result = num1 % num2
elif ope == "//":
    result = num1 // num2
elif ope == "**":
    result = num1 ** num2
else:
    result = "Invalid operator"
print("result", result)