## Lets learn how conditional statements work in python and why we use them in DSA
## Even or Odd
num = int(input())
if num%2 == 0:
    print("Even")
else:
    print("Odd")
## Largest of 2 numbers
a = int(input())
b = int(input())
if a>b:
    print("a is the greater number")
else: 
    print("b is the grater one")
## Check pass or fail
marks = int(input())
if marks >= 50:
    print("Pass")
else: 
    print("Fail")

## The HackRank Example
n = int(input())
if n%2 != 0:
    print("Weird")
else:
    if n>=2 and n<=5:
        print("Not Weird")
    elif n>=6 and n<=20:
        print("Weird")
    else:
        print("Not Weird")
        