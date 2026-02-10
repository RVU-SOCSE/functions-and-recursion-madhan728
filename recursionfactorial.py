def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("enter a number:"))

if num < 0:
    print("factorial is not defined for negative numbers.")
else:
    print(f"factorial of {num} is {factorial(num)}")
    
