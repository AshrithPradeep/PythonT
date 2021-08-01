# TASK ONE
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


# TASK TWO
#1. Write a python program to perform the following operations:
#If a number is divisible by 3 it should print “ConsAd” as a string
#If a number is divisible by 5 it should print “Python” as a string
#If a number is divisible by both 3 and 5 it should print “ConsAd - Python” as a string

x=int(input("Enter a number here :"))

if (a%3)==0 and (a%5)==0:
    print("ConsAd - Python")
elif (a%5)==0:
    print("Python")
elif (a%3)==0:
    print("ConsAd")

#2. Write a python program to perform the following operator based task:
# Ask user to choose the following option first:
#if user enter 1 : Addition
#if user enter's 2 : Subtraction
#if user enter 3: division
#if user enter 4: Multiplication
#if user enter 5: Average
#Ask user to enter two numbers and keep those numbers in variables num1 and num2 respectively for the first 4 options mentioned above.
# Ask the user to enter two more numbers as first and second for calculating the average as soon as the user chooses an option 5.
# At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”.

print("Choose one of the following operations by their number : 1 for Addition, 2 for Subtraction, 3 for Division, 4 for Multiplication, 5 for Average")
a=int(input())
print("Enter the first number :")
num1=int(input())
print("Enter the second number :")
num2=int(input())

if a == 1:
    res = float(num1 + num2)
    print('The result is :', res)

elif a == 2:
    res = float(num1 - num2)
    print('The result is :', res)

elif a == 3:
    res = float(num1 / num2)
    print("The result is :", res)

elif a == 4:
    res = float(num1 * num2)
    print("The result is:", res)

elif a == 5:
    sum = float(num1 + num2)
    res = float(sum / 2)
    print("The result is:", res)

else:
    print("choose an option between 1-5")

if res < 0:
    print("Negative Number")



#3. Write a program in python to implement the flow chart:

a=10
b=20
c=30
average=(a+b+c)/3
print("avg: ",average)
while average in range(10,31):
    if average >((a) and (b) and (c)):
        print("Average is greater than a,b and c")
        break
    elif average > ((a)and (b)):
        print("Average is greater than a,b and c")
        break
    elif average >((a)and (c)):
        print("The average is greater than a,c")
        break
    elif average >((b) and (c)):
        print("The average is greater than b,c")
        break
    elif average > (a):
        print("The average is just greater than a")
        break
    elif average > (b):
        print ("The average is just greater than b")
        break
    elif average > (c):
        print ("The average is just greater than c")
        break
    else:
        break

#4. Write a program in python to break and continue if the following cases occur:
# if user enters a negative number just break the loop and print " It's over"
# if user enters a positive number just continue the loop and print "good going"

a=int(input("Enter a number"))
while a in range(-10000,10000):
    if a <0:
        print("It's over")
        break
    if a>=0:
        print("Good going")
        a+=1
        continue

#5.  Write a program in Python which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200.
for i in range(2000,3200):
    if ((i%7==0) and (i%5!=0)):
        print(i)

#6. What is the output of the following code snippets
x=123
for i in x:
    print(i)
## Type Error - int not iterable.

i=0
while i<5:
    print(i)
    i+=1
if i==3:
    break
else:
    print("error")
# Break can be used inside the loop and here it is outside it, so it throws an error for the same

count=0
while True:
    print(count)
    count +=1
    if count>=5:
        break
# prints 01234 and then breaks due to the condition

#7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.

i=0
while i in range(0,7):
    if i == 3 or i ==6:
        i+=1
        continue
    print(i)
    i+=1

#8. Write a program that accepts a string as an input from the user and calculate the number of digits and letters.
x = input("enter the string")
number, alphabet = 0,0
for y in x:
    if y.isdigit():
        number+=1
    elif y.isalpha():
        alphabet+=1
    else:
        pass
print("alphabets:", alphabet )
print("numbers:", number)

#9.Read the two parts of the question below:
#Write a program such that it asks users to “guess the lucky number”. If the correct number is guessed the program stops, otherwise it continues forever.
#Modify the program so that it asks users whether they want to guess again each time. Use two variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want
#to continue guessing. The program stops if the user guesses the correct number or answers “no”. ( The program continues as long as a user has not answered “no” and has not guessed the correct number)

number = int(input("Guess the lucky number here:  "))
while number != 9:
    print("You have not guessed the lucky number")
    number = int(input("guess the lucky number again:  "))

# Modified version
again = "yes"
number = int(input("Guess the lucky number"))
while number != 9:
    print("You have not guessed the lucky number")
    again = (input("guess again?"))
    if again == "no":
        break
    else:
        number = int(input("Guess the lucky number"))
        if number == 9:
            print("you win!!!!!!!")

#10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter, such as While counter <= 5: print(“Type in the”, counter, “number” counter=counter+1
# The program asks for five guesses (no matter whether the correct number was guessed or not). If the correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
#After the fifth guess it stops and prints “Game over!”.

counter = 1
while counter <= 5:
   if counter == 5:
       print("sorry your attempts were not successful")
       break
   num = int(input("Guess the number"))
   if num == 5:
       print ("Good guesss.")
       break
   else:
       print ("try again!")
   counter +=1


else:
   print ("game over")

#11.In the previous question, insert break after the “Good guess!” print statement. break will terminate
#the while loop so that users do not have to continue guessing after they found the number. If the user
#does not guess the number at all, print “Sorry but that was not very successful”.

counter = 1
while counter <= 5:

    num = int(input("Guess the number"))

    if num == 5:
        print("Good guesss.")
        break
    else:
        if counter == 5:
            print("sorry your attempts were not successful")
            break
        else:
            print("try again!")
    counter += 1

print("game over")