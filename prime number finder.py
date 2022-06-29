import os
import time
import random

number = random.randint(1,100)
name = input("Enter your name: ")
os.system('cls' if os.name == 'nt' else "printf '\033c'")
turns=0
x = 0

bigger = 0
smaller = 100
while x==0:
  
  print("You have had "+str(turns)+" turns!")
  time.sleep(1)
  guess=int(input("\nWhat number are you going to guess (Between 1 and 100) "+name+": "))
  if guess > bigger:
    bigger = guess
  if guess < smaller:
    smaller = guess
  time.sleep(1)
  if guess < number:
    print("\nYour number is to low, you are stupid "+str(name)+"\n")

  if guess > number:
    print("\nYour number is to high, you are stupid "+str(name)+"\n")

  elif guess == number:
    print("\nYou guessed correct "+str(name)+"\n")
    x=x+1
  turns=turns+1
  time.sleep(2)
  print("Your biggest guess so far is "+str(bigger)+"!\n")
  time.sleep(1)
  print("Your smallest guess so far is "+str(smaller)+"!\n")
  
  time.sleep(2)
  os.system('cls' if os.name == 'nt' else "printf '\033c'")

print("You win")
