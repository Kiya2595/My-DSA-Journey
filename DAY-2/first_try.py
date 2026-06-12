#Lets practice % and // operators on real small DSA problem
#Sum of digits
num = int(input("Enter a number: "))
sum_of_digits = 0
while num > 0:
    digit = num % 10
    sum_of_digits += digit
    num = num // 10
    print("Digit: ", digit)
    print("Sum of digits: ", sum_of_digits)
print("Final sum of digits: ", sum_of_digits)