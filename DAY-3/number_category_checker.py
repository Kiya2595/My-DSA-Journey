## A Small Practice
n = int(input("Enter a number:"))
if n<=0:
    print("INVALID")
elif n<=10:
    print("SMALL")
elif n<=100:
    print("MEDIUM")
else:
    print("LARGE")