#1. Write a program that calculates and prints the value according to the given formula:
# Q= Square root of [(2*C*D)/H]
# Following are the fixed values of C and H:
# C is 50.
# H is 30.
# D is a variable whose values should be input to your program in a comma-separated sequence.
import math
input = input("Enter the value of D: ")
input = input.split(',')
C = 50
H = 30
temp = []
for D in input:
    Q = round(math.sqrt(2 * C * int(D) / H))
    temp.append(Q)
print(temp)

#2. Define a class named Shape and its subclass Square. The Square class has an init function which
#takes length as argument. Both classes have an area function which can print the area of the shape
#where Shape’s area is 0 by default.
class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.len = l

    def area(self):
        return self.len*self.len

aSquare= Square(4)
print (aSquare.area())

#3. Create a class to find three elements that sum to zero from a set of n real numbers
# Input array: [-25,-10,-7,-3,2,4,8,10]
# Expected output: [[-10,2,8],[-7,-3,10]]
# def sum(self, nums: List[int]) -> List[List[int]]:
list = [-25, -10, -7, -3, 2, 4, 8, 10]
final = set()
list.sort()
for i in range(len(list) - 2):
    low = i + 1
    high = len(list) - 1
    while low < high:
        if list[i] + list[low] + list[high] < 0:
            low += 1
        elif list[i] + list[low] + list[high] > 0:
            high -= 1
        else:
            final.add((list[i], list[low], list[high]))
            low += 1
            high -= 1
print(list(final))

#4.Create a Time class and initialize it with hours and minutes.
# Create a method addTime which should take two Time objects and add them.
# E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
# Create another method displayTime which should print the time.
# Also create a method displayMinute which should display the total minutes in the Time.
class Time():

    def __init__(self, hrs, mins):
        self.hrs = hrs
        self.mins = mins

    def addTime(x, y):
        z = Time(0,0)
        if x.mins+y.mins > 60:
            z.hrs = (x.mins+y.mins)/60
        z.hrs = z.hrs+x.hrs+y.hrs
        z.mins = (x.mins+y.mins)-(((x.mins+y.mins)/60)*60)
        return z

    def displayTime(self):
        print("Time is",self.hrs,"hours and",self.mins,"minutes.")

    def displayMinute(self):
        print((self.hrs*60)+self.mins)

time1 = Time(2,50)
time2 = Time(1,20)
sum = Time.addTime(time1,time2)
sum.displayTime()
sum.displayMinute()

#5. Write a Person class with an instance variable “age” and a constructor that takes an integer as a
# parameter. The constructor must assign the integer value to the age variable after confirming the
# argument passed is not negative; if a negative argument is passed then the constructor should set
# age to 0 and print “Age is not valid, setting age to 0”. In addition, you must write the following instance
# methods:

# yearPasses() should increase age by the integer value that you are passing inside the function.
# amIOld() should perform the following conditional actions:I
# f age is between 0 and <13, print “You are young”.
# If age is >=13 and <=19 , print “You are a teenager”.
# Otherwise, print “You are old”.

class Person:
    def __init__(self,present_age):
        if present_age < 0:
            self.age = 0
            print("Age is not valid, setting age to 0.")
        else:
            self.age = present_age
    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif self.age>=13 and self.age <18:
            print("You are a teenager.")
        else:
            print("You are old.")
    def yearPasses(self,yrs):
        self.age = self.age + yrs
        return self.age
obj = Person(int(input("enter age: ")))
obj.yearPasses(int(input("enter number of years you wanna grow older: ")))
obj.amIOld()


