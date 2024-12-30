
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# getting list from user using for loop 
numbers = []
n = int(input("Enter the number of elements: "))
for i in range( n ):
    numbers.append(int(input("Enter a number: ")))
    
print("The average is:", calculate_average(numbers))
