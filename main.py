#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letterLen=len(letters)-1
numbersLen=len(numbers)-1
symbolsLen=len(symbols)-1
letterList=[]
for l in range(0,nr_letters):
  letterList.append(letters[random.randint(0,letterLen)])

numberList=[]
for l in range(0,nr_numbers):
  numberList.append(numbers[random.randint(0,numbersLen)])

symbolList=[]
for l in range(0,nr_symbols):
  symbolList.append(symbols[random.randint(0,symbolsLen)])  

combined=letterList+numberList+symbolList
random.shuffle(combined)
# print(combined)
strf=""
for x in combined:
  strf+=x

print("Your password should be: "+strf)  
