numbers = [1,2,3,4,5,6,7,8,9,10]

even_numbers = []
even_count = 0 #store count of even numbers

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
        
        #increment count of even numbers
        even_count += 1
        
print(even_numbers)
print('There are', even_count, 'even numbers in the list.')

##Write a code that finds the min value of a list of numbers.
##5,3,8,-1,-2.2,0

list2 = [5,3,8,-1,-2.2,0]

#Keep track of min value
min_value = list2[0]

for number in list2:
    if number < min_value:
        min_value = number
print(min_value)
    
#Using a for loop print each letter of the name on the same line, count each letter in the name, and print the 
#count of letters in the name

name = input('Enter your name: ')

countName = 0

for letter in name:
    print(letter, end =' ')
    countName += 1
print('')
print('There are: ', countName, 'letters in the name.')

##While lopp

inpt = ''
while inpt != 'secret':
        inpt = input('Enter a password: ')
        if inpt == 'secret':
            print('Welcome!')
        else:
            print('Sorry, the password you entered is incorrect. Please try again.')
            
##Exit a loop using break

x = 1
while x <= 10:
    if x == 5:
        break
    print(x)
    x += 1
    
for number in range(1,21):
    
    #test for odd number
    if (number % 2) != 0):
        #test for multiple of 3
        if (number % 3) == 0:
            continue
        print(number)
