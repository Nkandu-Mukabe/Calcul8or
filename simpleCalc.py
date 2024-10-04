num1 = input("Enter your first number: ")
op = input("Enter an operator: ")
num2 = input("Enter your second number: ")

if op == "+":
    answer = float(num1) + float(num2)
    # print the answer here rather than storing it in an extra var
elif op == "-":
    answer = float(num1) - float(num2)
elif op == "/":
    answer = float(num1) / float(num2)
elif op == "*":
    answer = float(num1) * float(num2)
# can put the float function around the num declaration to make it easier
# i.e. num1 = float(input("etc"))
else:
    answer = "there was an error with your input, try again later"

print(answer)
