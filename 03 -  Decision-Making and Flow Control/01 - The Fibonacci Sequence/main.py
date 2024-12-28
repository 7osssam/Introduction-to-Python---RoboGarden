
user_input = int(input("How many numbers of the Fibonacci Sequence would you like to generate? "))

# using loops
if (user_input < 0 ):
	print("Please enter a valid number")
	exit()

for index in range(user_input):
	if index == 0:
		fibonacci = [0]
	elif index == 1:
		fibonacci.append(1)
	else:
		fibonacci.append(fibonacci[index-1] + fibonacci[index-2])


print(fibonacci)
