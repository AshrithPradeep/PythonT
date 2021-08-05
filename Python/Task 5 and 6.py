#1. Write a program in Python to allow the error of syntax to be handled using exception handling.
try:
    eval('a***b')
except SyntaxError:
    print("syntax error raised.")

#2. 2.	Write a program in Python to allow the user to open a file by using the argv module.
# If the entered name is incorrect throw an exception and ask them to enter the name again. Make sure to use read only mode.
import sys
def file_open(temp):
    try:
        if sys.argv[0] == temp:
            with open(temp, 'r') as o:
                o.read()
        raise FileExistsError("wrong file, enter the name again: ")
    except FileExistsError:
        raise
file_open(input('user_input:  '))

#3. Write a program to handle an error if the user entered a number more than four digits it should
#return “The length is too short/long !!! Please provide only four digits”

def num_check(num):
    try:
        if len(str(num))>4:
            raise ValueError("you can only enter 4 digit number")
        elif len(str(num))<=3:
            raise ValueError("4 digits required")
        print(num)
    except:
        print("Please provide only four digits number.")
        raise


num_check(eval(input('enter number: ')))

#4.
tries = 0
while tries<3:
    name = (input("enter a name: "))
    password = (input("enter a password: "))
    re_type = (input("re type your password: "))
    tries +=1
    if (password == re_type):
        print("login successfull")
        break
    else:
        if(tries<3):
            print("something went wrong!! try again...")
        elif(tries==3):
            print("maximum allowed attempts exhausted!!")

#6. Read doc.txt file using Python File handling concept and return only the even length string from
# the file.
with open('doc.txt', 'w') as text:
    text.write("Hello I am a file\nWhere you need to return the data string\nwhich is of even length")
    text.write('\nMake sure you return the same link as it is present')
with open("doc.txt") as text:
    result = ""
    for i in text:
        read = i.split()
        for j in read:
            if len(j) % 2 == 0:
                result = result + " " + j

print(result)


#TASK 6
#1. Write a program in Python to find out the character in a string which is uppercase using list
#comprehension.
string = (input("enter a string: "))
final = [i for i in string if i.isupper()]
print(final)

#2. Write a program to construct a dictionary from the two lists containing the names of students and
# their corresponding subjects. The dictionary should map the students with their respective subjects.
# Let’s see how to do this using for loops and dictionary comprehension.
students = ['Smit', 'Jaya', 'Rayyan']
subjects = ['CSE', 'Networking', 'Operating System']
result = {key:values for key,values in zip(students,subjects)}
print(result)

#4.Write a program in Python using generators to reverse the string.
def reverse(str):
    length = len(str)
    for i in range(length - 1, -1, -1):
        yield str[i]
input = "ConsAd"
for char in reverse(input):
    print(char)

#5.Write an example for decorator
def exampleDecorator(func):
    def extrafunction():
        print("This is the added text to the actual function.")
        func()
    return extrafunction

@exampleDecorator
def actualFunction():
    print("This is the actual function.")

actualFunction()