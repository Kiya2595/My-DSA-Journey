## Lets understand loops 
## TASK 1: Print Numbers 1 to N
n = int(input("Enter a number: "))
for i in range(1, n+1):
    print(i)

## TASK 2: Sum of the first N numbers
total = 0
for i in range(1, n+1):
    total += i
print("Sum of first", n, "numbers is: ", total)

## TASK 3: Filtering Values
for i in range(1, n+1):
    if i%2 == 0:
        print(i)
 
## HackRank Example
n = int(input("Enter the number: "))
for i in range(0, n):
    print(i*i)