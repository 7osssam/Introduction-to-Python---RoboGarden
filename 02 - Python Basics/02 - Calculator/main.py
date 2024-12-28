
def calculator() -> None:
	num1 = int(input("Enter the first number: "))
	num2 = int(input("Enter the second number: "))
	operator = input("Enter the operator (+, -, *, /): ")

	if not num1.isdigit() or not num2.isdigit():
		print("Please enter a valid number")
		return

	if operator not in ["+", "-", "*", "/"]:
		print("Please enter a valid operator")
		return

	if operator == "+":
		result = num1 + num2
	elif operator == "-":
		result = num1 - num2
	elif operator == "*":
		result = num1 * num2
	elif operator == "/":
		if num2 == 0:
			print("Cannot divide by zero")
			return
		result = num1 / num2

	print(f"The result of {num1} {operator} {num2} is {result}")


calculator()