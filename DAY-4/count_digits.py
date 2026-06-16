## Lets count the number of digits in a number using while loop
num = int(input("Enter a number:"))
count = 0
while num > 0:
    num = num // 10
    count += 1
print("Number of digits: ", count)

## Count Even and Odd numbers in the range of 1 to N
n = int(input("Enter a number: "))
even_count = 0
odd_count = 0
for i in range(1, n+1):
    if i%2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even: ", even_count)
print("Odd: ", odd_count)
