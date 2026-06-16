## Lets see function in DSA a littile bit 
## Sum of digits
n = int(input("Enter number: "))
def sum_digit(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n//10
    return total
print(sum_digit(n))

## Check even or odd
n = int(input("Enter the number you want to know: "))
def check_even_or_odd(n):
    if n%2 == 0:
        print("Even")
    else:
        print("Odd")
check_even_or_odd(n) 

## Factorial
n = int(input("Enter the number: "))
def factorial(n):
    for i in range(1, n+1):
        result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

print(factorial(n))