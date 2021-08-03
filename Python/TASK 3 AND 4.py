# 1. Create a list of 10 elements of four different data types like int, string, complex and float.
a = [1,2,3,4,5,6,"string",3.8, 11+10j,"10"]

#2. Create a list of size 5 and execute the slicing structure

a =[1,2,3,4,5]
print(a[1:5])

#3.  Write a program to get the sum and multiply of all the items in a given list.
sum = 0
product = 1
list = eval(input("enter the elements: "))
for i in list:
    sum = sum + i
    product = product * i

print(sum, product)

#4. Find the largest and smallest number from a given list.
list = eval(input("enter list: "))
min = list[0]
max = list[0]

for i in range(len(list)):
    if list[i]  < min:
        smallest = list[i]

    if list[i] > max:
        max = list[i]

print("min is: ", min)
print("max is: ", max)


#5. Create a new list which contains the specified numbers after removing the even numbers from a
# predefined list.
list1 = eval(input("enter elements: "))
updated = list(filter(lambda x:x % 2 !=0,list1))
print(updated)

#6. Create a list of elements such that it contains the squares of the first and last 5 elements between
#1 and30 (both included).
final = []
for i in range(1, 31):
    if i < 6 or i > 25:
        final.append(i ** 2)

print(final)

#7. Write a program to replace the last element in a list with another list.
#Sample input: [1,3,5,7,9,10], [2,4,6,8]
#Expected output: [1,3,5,7,9,2,4,6,8]

a=[1,3,5,7,9,10]
b=[2,4,6,8]
a[-1:]=b
print(b)

#8. Create a new dictionary by concatenating the following two dictionaries:
#Sample input: a={1:10,2:20} b={3:30,4:40}
#Expected output: {1:10,2:20,3:30,4:40}

a = eval(input("dict1: "))
b = eval(input("dict2: "))
c=dict(a)
c.update(b)
print(c)

#9. Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1
#and n(both 1 and n included).
#Sample input: n=5
#Expected output: {1:1, 2:4, 3:9, 4:16, 5:25}
n = int(input("enter n: "))
d = {}
for i in range(1,n+1):
    d[i]=i*i

print(d)

#10. Write a program which accepts a sequence of comma-separated numbers from console and
#generates a list and a tuple which contains every number in the form of string.
#Sample input: 34,67,55,33,12,98
#Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’)
a = input("enter elements: ").split(",")
t = tuple(a)
print('list:', a)
print('tuple:', t)

##TASK4

#1.Write a program to reverse a string.

string = input("enter string: ")
temp = []
length = len(string)
while length:
    length -= 1
    temp.append(string[length])
print(''.join(temp))

#2. Write a function that accepts a string and prints the number of uppercase letters and lowercase
# letters.

def count():
    strings = input("enter string: ")
    upper = 0
    lower = 0
    for i in range(len(strings)):
        if strings[i].isupper():
            upper +=1
        elif strings[i].islower():
            lower +=1
    print("upper: ", upper)
    print("lower: ", lower)

count()

#3. Create a function that takes a list and returns a new list with unique elements of the first list.
list = list(input("enter the elements: "))
final = []
for i in list:
    if list.count(i)==1:
        final.append(i)
print(final)

#4.  Write a program that accepts a hyphen-separated sequence of words as input and prints the words
# in a hyphen-separated sequence after sorting them alphabetically.
def sort_alpha():
    args = input("enter hypen separated words: ").split("-")
    print(args)
    args.sort()
    return ("-").join(args)

print(sort_alpha())

#5.Write a program that accepts a sequence of lines as input and prints the lines after making all
#characters in the sentence capitalized.
def upper():
    args = input("enter string: ")
    return args.capitalize()

print(upper())

#6. Define a function that can receive two integral numbers in string form and compute their sum and
#print it in the console.

a,b = (input("enter the numbers ")).split("")
a = int(a)
b = int(b)
sum = lambda a,b : a + b
print(sum(a,b))

#7. Define a function that can accept two strings as input and print the string with the maximum length
#in the console. If two strings have the same length, then the function should print both the strings line
#by line.

a=input("enter string")
b=input("enter string")
len_A=len(a)
len_B=len(b)
if len_A>len_B:
    print(a)
elif len_B>len_A:
    print(b)
else:
    print(a)
    print(b)

#8. Define a function which can generate and print a tuple where the values are square of numbers
#between 1 and 20 (both 1 and 20 included).
def sqrt():
    a= []
    for i in range(1,21):
        square = i * i
        a.append(square)

    print(tuple(a))
sqrt()

#9.  Write a function called showNumbers that takes a parameter called limit. It should print all the
# numbers between 0 and limit with a label to identify the even and odd numbers.

def showNumbers():
    max = int(input("enter number"))
    for i in range(max + 1):
        if i % 2 != 0:
            print(i , "ODD")
        elif i % 2 == 0:
            print(i, "EVEN")

showNumbers()

#10. Write a program which uses filter() to make a list whose elements are even numbers between 1
# and 20 (both included)
a = list(range(1,21))
even = lambda x: x % 2 == 0
print(list(filter(even, a)))

#11.Write a program which uses map() and filter() to make a list whose elements are squares of even
#numbers in [1,2,3,4,5,6,7,8,9,10].
#Hints: Use filter() to filter even elements of the given listUse map() to generate a list of squares of the
#numbers in the filtered list. Use lambda() to define anonymous functions.
def square():
    a = list(range(1,11))
    even = list(filter(lambda x: x % 2 ==0,a))
    sqr =lambda x: x * x
    print(list(map( sqr, even)))

square()

#12.
def divide():
    try:
        print(5 / 0)
    except ZeroDivisionError as z:
        print("cant divide by zero")

divide(int(input("enter number 1: ",)), int(input("enter number 2: ")))

#13. Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().
import functools
dl =""
list1 = list(range(1,8))
reduce_num = functools.reduce(lambda a, b: str(a) + dl + str(b),list1)
print(reduce_num)

#14.  Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
# Make sure to use only higher order functions.
print(list(filter(lambda x: x % 7 ==0 and x % 3 !=0, eval(input("enter elements: ")))))

#15.Write a program in Python to multiply the elements of a list by itself using a traditional function
# and pass the function to map() to complete the operation.

def product(list1):
    return list1 * list1

list2 = list(eval(input("enter a list: ")))
print(list(map(product, list2)))

#16.

#ANS 1 : 2
#ANS 2 : print statements work but later when function f is called it doesnt work as it isnt defined.