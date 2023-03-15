"""This code will
Prompt for your name
Set the name variable
Print a message"""

name = input('What is your name?')
print('Hello ' + name)

# Set variable x to cats
# Set a varib
# lae y to dogs

x = 'cats'
y = 'dogs'
s = "It's raining " + x + " and " + y + "!"

#Print the message
print(s)

fav_colour = input("What is your favourite color?")
favs = "Your favourite colour is " + fav_colour
fav_colour = "Your favourite colour is {}".format(fav_colour)

#Variables Exercise
#Calculate the total bill at a restaurant (meal + tax + tip)

#1. Prompt the user for the bill amount, the sales tax and the tip percentage
billPreTax = input("What is the total bill?")
taxPercentage = input("What is the sales tax?")
tipPercentage = input("What is the tip percentage?")

#2. Calculate the total bill

totalBill = billPreTax + (billPreTax * (taxPercentage/100))
totalBill = totalBill + (totalBill * (tipPercentage/100))

#3. Print the total bill

print(totalBill)

