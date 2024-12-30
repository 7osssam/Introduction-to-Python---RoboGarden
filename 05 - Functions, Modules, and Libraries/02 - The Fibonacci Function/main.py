
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
user_input = int(input("Enter a number: "))
print(f"The Fibonacci sequence of {user_input} is {fibonacci(user_input)}")
