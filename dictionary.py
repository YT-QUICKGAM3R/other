import time
import random
import sys
import os




#Storing a item to a variable
name = "Jacob Cook"


#Storing a string from an input to a variable
name = input("What is your name?")



#Storing a interger from an inpuy to a variable
age = int(input("How old are you?"))



#Decsions from if statments
if age <16:
  print("Your to young!")
elif age >=16:
  print("Your allowed in!")


#Counting up to a number using a for loop
for x in range(1, age+1):
  print(x)
  time.sleep(0.1)

#Counting up to 100 using a while loop
x=0
while x <100:
  x=x+1
  print(x)
  time.sleep(1)


#List of favourite foods
fav_food=["Pizza", "Curry", "Lasagna"]
print(fav_food)
#Print a list place
print(fav_food[0])


#Divide
AdivB = 10/2
print(int(AdivB))


#Multiply
AtimesB = 10*2
print(int(AtimesB))


#Takeaway
AtakeB = 10-2
print(int(AtakeB))


#Add
AaddB = 10+2
print(int(AaddB))

#divide but round down
AdivB = 11//3

#Denary to Binary
number = int(input("Enter any decimal number: "))
print("Equivalent Binary Number: ", bin(number))

#List positions
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))

#Add to a list
fruits.append('grape')
print(fruits)


#print a number with formating
str(f"{Example:,}")

#clear all
print("\033[H\033[J")

#print letter by letter
words = "WHAT YOU WANT TO PRINT"
for char in words:
    time.sleep(0.05) #time inbetween each char
    sys.stdout.write(char)
    sys.stdout.flush()

#Repeat once loading, change the range to change repeats
for i in range(1):
  os.system('clear')
  print("Loading")
  time.sleep(0.3)
  os.system('clear')
  print("Loading.")
  time.sleep(0.3)  
  os.system('clear')
  print("Loading..")
  time.sleep(0.3)
  os.system('clear')
  print("Loading...")
  time.sleep(0.3)  
  os.system('clear')
  time.sleep(1)

#other type of loading screen

def loading():
  print("\033[H\033[J")
  sys.stdout.write("\rloading |")
  time.sleep(0.1)
  sys.stdout.write("\rloading /")
  time.sleep(0.1)
  sys.stdout.write("\rloading -")
  time.sleep(0.1)
  sys.stdout.write("\rloading \\")
  time.sleep(0.1)
  sys.stdout.write("\rloading |")
  time.sleep(0.1)
  sys.stdout.write("\rloading /")
  time.sleep(0.1)
  sys.stdout.write("\rloading -")
  time.sleep(0.1)
  sys.stdout.write("\rloading \\")
  time.sleep(0.1)
  sys.stdout.write("\rloading |")
  time.sleep(0.1)
  sys.stdout.write("\rloading /")
  time.sleep(0.1)
  sys.stdout.write("\rloading -")
  time.sleep(0.1)
  sys.stdout.write("\rloading \\ \n")
  time.sleep(0.1)
  print("\033[H\033[J")

#split up words n ammount of times

s = 'lipsum'
n = 4
a, s = s[:n], s[n:]
print(a)
#prints 'lip'
print(s)
#prints 'sum'
