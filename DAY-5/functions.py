## Lets now understand Function
## TASK 1: Basic Function
def greet():
    print("My name is FEVEN")
greet()

## TASK 2: Add 2 numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
def add(a, b):
    return a + b
sum = add(a, b)
print(sum)

##HackerRank Example
def is_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

year = int(input())
print(is_leap(year))

