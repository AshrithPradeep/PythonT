#1. Create a list of given structure and get the Access list as provided below:
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
print(x[[5][:4]])
print(x[-3:])
print(x[::2])
print(x[::-1])
print([x[5][5][0]])
print(list())

#2. Create a list of thousand numbers using range and xrange and see the difference between each other.

print(list(range(1001)))
print(list(xrange(1001)))
# one major difference is that the range function returns a list type object, whereas an xrange function returns an xrange type object.

#3. How Tuple is beneficial as compared to the list?
# Tuples are faster than lists as they have constant set of values. Tuples are stored in a single block of memory and they're immutable
# so they dont require extra memory. Creating and indexing speed is faster in tuples.

#4. Write a program in Python to iterate through the list of numbers in the range of 1,100 and print
# the number which is divisible by 3 and is a multiple of 2.

final=[]
for i in range(1,101):
    if(i%3==0) and (i%2):
        final.append(str(i))
print(final)

#5.Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the string with their index.
str = "ashrith"
str = str[::-1]
print(str)
for i, vowel in enumerate(str):
    if vowel.lower() in 'aeiou':
        print(i,vowel)

#6.Write a program in Python to iterate through the string “hello my name is abcde” and print the string which is having an even length.
str = "hello my name is abcde rama”
a = str.split(" ")
for i in a:
    if len(i) %2 == 0:
        print(i)

#7. Write a program in python to print the pair of numbers whose sum is equal to the result number that is let's say 8.
x=[1,2,3,4,5,6,7,8,9,-1]
s = []
target =8
for i in x:
    temp = target - i
    if temp in s:
        print(i, temp)
    s.append(i)

#8. Write a program in Python to complete the following task:
#Create two lists such as even_list and odd_list
#Ask user to enter a number in the range of 1,50 and make sure if the entered number is
#even, append it to the even_list and if the entered number is odd append it to the odd_list.
#Keep that in mind you can only add 5 items in each list
#Make sure once you enter all the 5 elements, calculate the sum of the list and return the
#maximum of the list.

even = []
odd = []
while len(even) < 5 or len(odd) < 5:
    a = int(input("enter a number in the range 1 and 50: "))
    if a % 2 == 0:
        if len(even) < 5:
            even.append(a)
        else:
            pass
    else:
        if len(odd) < 5:
            odd.append(a)
        else:
            pass
else:
    pass

print("sum of even is: " + str(sum(even)) + " and max element of even is " + str(max(even)))
print("sum of even is: " + str(sum(odd)) + " and max element of even is " + str(max(odd)))
print("max between even and odd is: ", str(max(sum(even), sum(odd))))

#9.Write a program to find out the occurrence of a specific character from an alphanumeric string.
def count():
    string = str(input("enter strings: "))
    frequency = {}
    for i in string:
        if i in "abcdefghijklmnopqrstuvwxyz":
            frequency[i] = string.count(i)

    for a, b in frequency.items():
        print(str(a)+"="+str(b))


count()

#10.Generate and print another tuple whose values are even numbers in the given tuple
def even(num):
    return tuple(filter(lambda x: x % 2 == 0,num))

print(even(range(1,11)))