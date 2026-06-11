#Data types
name = "Feven" #string 
acadamic_year = 3 #int
height = 1.60 #float
is_student = True #boolean 
print("-----User Info-----")
print("Name: ",name)
print("Acadamic Year: ",acadamic_year)
print("Height: ",height)
print("Is Student: ", is_student)

#and also we can know the type of the data by using type() function
print("-----Data Types-----")
print(type(name))
print(type(acadamic_year))
print(type(height))
print(type(is_student))

#we can convert one data type to another by using type conversion functions
#for example we can convert an integer to a string by using str() function
acadamic_year_str = str(acadamic_year)
print(acadamic_year_str)

#in python we can also use the input() function to get user input and it will always return a string
department = input("Enter your deparment: ")
print("Your department is: " + department)

#as i mentioned before the input() function will always return a string, so if we want to convert it to another data type we can use the type conversion functions
#for example if we want to convert the input to an integer we can use int() function
age = int(input("Enter your age:"))
print("Your age is: ", age)
next_year_age = age + 1
print("Next year you will be: ", next_year_age)