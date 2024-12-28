
num = int(input("Enter a number: "))

if num < 0:
	print("Please enter a positive number")
	exit()

factorial = 1

for i in range(1, num + 1):
	factorial *= i

print(f"The factorial of {num} is {factorial}")