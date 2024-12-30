
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    

user_input = int(input("Enter a number: "))
print(f"The factorial of {user_input} is {factorial(user_input)}")