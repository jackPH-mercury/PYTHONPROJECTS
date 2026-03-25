# Simple Four-Function Calculator
print("--- Python Console Calculator ---")
print("Select operation: +, -, *, /")
# 1. Take user input for the operation
operation = input("Enter operation: ")
# 2. Take user input for numbers (converted to floats)
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
# 3. Perform the calculation based on the operation
# conditiional operation
if operation == '+': # note ==
result = num1 + num2
print(f"{num1} + {num2} = {result}")
# read this as else if
elif operation == '-':
result = num1 - num2
print(f"{num1} - {num2} = {result}")
elif operation == '*':
result = num1 * num2
print(f"{num1} * {num2} = {result}")
elif operation == '/':
# Check for division by zero
if num2 != 0:
result = num1 / num2
print(f"{num1} / {num2} = {result}")
else:
print("Error: Cannot divide by zero.")
# handle no match case
else:
print("Invalid operation selected.")
