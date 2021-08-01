# 1. Create three variables in a single line and assign values to them in such a manner that each one of
# them belongs to a different data type.
a,b,c = 1, 2.0, 'ashrith'

# 2. Create a variable of type complex and swap it with another variable of type integer.
a = 2 +1j
b = 1

a,b = b,a

#3. Swap two numbers using a third variable and do the same task without using any third variable.
#by using third variable
a,b = 1,2
temp = a
a = b
b = temp

#without using third variable
a,b = b,a

#4.Write a program that takes input from the user and prints it using both python 2x. and python 3.x version

a = eval(raw_input("enter a number"))
print(a)

b = eval(raw_input("Enter a number"))
print(b)

#5. Write a program to complete the task given below: Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
#another variable called z. Add 30 to z and store the output in variable result and print result as the final output.

a = int(input("enter number 1 :"))
b = int(input("enter number 2 :"))
print(a,b)
z = a+b
result = z+30
print(z)

#6.  Write a program to check the data type of the entered values.

a = eval(input("enter the value"))
print(type(a))

#7. Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and UPPERCASE.

UpperCamel = 1
lowerCamel = 2
snake_case = 3
UPPERCASE = 4

#8 If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’
#again. Will it change the value? If Yes then Why?
# ANSWER : Yes, the value changes as we assign a value of different data type, because the first one is saved in one memory location and the second one in another.
# So the variable changes its datatype



