def square(x):
    return x * x

result = square(10)
print(result)

def greater_than(x, y):
    if x > y:
        return True
    else:
        return False

resultF = greater_than(2, 3)

def get_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

factors = get_factors(10)

def fun1(num):
    return num + 25

fun1(5)


def vowel_count(word):
    """Counts the number of vowels in a word"""
    
    count = 0
    #iterate through each letter in the word
    for char in word:
        #check if the letter is a vowel
        if char in 'aeiou':
            count += 1
    return count


    main()
        
