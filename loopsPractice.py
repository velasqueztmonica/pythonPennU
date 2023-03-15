num_list = []
i =0
playing = True

while playing == True:
    num = int(input('Enter a number: '))
    #test if number is negative -1 to exit the programm
    if num == -1:
        playing = False
    else:
    #add number to list of numbers    
        num_list.append(num)
        i += 1
#get the sum of all enter numbers
num_sum = 0
for num in num_list:
    num_sum += num
#calculate the average
num_average = num_sum / i
print('The average of the entered numbers is: ', num_average)

#Programme that reverses a word in a sentence

string = 'pasta'
rev = ''
print(len(string))

for j in range(len(string) - 1, -1, -1):
    #concatne character at index j with character at index j + 1
    rev += string[j]
    
print(rev)
