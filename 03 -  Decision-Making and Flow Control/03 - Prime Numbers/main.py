
num = int(input("Enter a number: "))

if num < 0:
	print("Please enter a positive number")
	exit()

if num == 0 or num == 1:
	print(f"{num} is not a prime number")
	exit()

for i in range(2, num):
	if num % i == 0:
		print(f"{num} is not a prime number")
		break
else:
	print(f"{num} is a prime number")

