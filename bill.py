#Variables Exercise
#Calculate the total bill at a restaurant (meal + tax + tip)

#1. Prompt the user for the bill amount, the sales tax and the tip percentage
billPreTax = int(input("What is the total bill?"))
taxPercentage = int(input("What is the sales tax?"))
tipPercentage = int(input("What is the tip percentage?"))

#2. Calculate the total bill

totalBill = billPreTax + (billPreTax * (taxPercentage/100))
totalBill = totalBill + (totalBill * (tipPercentage/100))
totalBill = round(totalBill,2) # round the total bill to 2 decimal places

#3. Print the total bill

print('The total bill is $', totalBill, sep = '')

