def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = 5  # change this number as needed
print(f"The factorial of {num} is {factorial(num)}")
