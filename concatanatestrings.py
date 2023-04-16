def concatenate(strings):
    
    """
    Concatenates the given list of string into a single string.
    Returns the single string.
    If the given list is empty, return an empty string.
    
    For example:
    - If we call the concatenate(['a', 'b', 'c']), we'll get the 'abc' in return
    """
    
    #Code below
    if strings == []:
        return ""
    else:
        listJoin = ''.join(strings)
        return listJoin

concatenate([])

def all_but_last(seq):
    """
    Returns a new list containing all but the last element in the given list.
    If the list is empty, returns None.

    For example:
    - If we call all_but_last([1,2,3,4,5]), we'll get [1,2,3,4] in return
    - If we call all_but_last(["a","d",1,3,4,None]), we'll get ["a","d",1,3,4] in return
    - If we call all_but_last([]), we'll get None in return
    """
    # your code here
    if  seq == []:
        return None
    else:
        seq.pop()
        print(seq)
        return seq

        
all_but_last([1,2,3,4,5])

def remove_duplicates(lst):
    """
    Returns the given list without duplicates.
    The order of the returned list doesn't matter.

    For example:
    - If we call remove_duplicates([1,2,1,3,4]), we'll get [1,2,3,4] in return
    - If we call remove_duplicates([]), we'll get [] in return

    Hint(s):
    - Remember, you can create a set from a string, which will remove the duplicate elements
    """
    
    # your code here
    new_List = list(set(lst))
    return new_List

def reverse_word(word):
    """
    Reverses the order of the characters in the given word.

    For example:
    - If we call reverse_word("abcde"), we'll get "edcba" in return
    - If we call reverse_word("a b c d e"), we'll get "e d c b a" in return
    - If we call reverse_word("a  b"), we'll get "b  a" in return
    - If we call reverse_word(""), we'll get "" in return

    Hint(s):
    - You can iterate over a word in reverse and access each character
    """
    
    # your code here
    return word[::-1]

def divisors(n):
    """
    Returns a list with all divisors of the given number n.
    As a reminder, a divisor is a number that evenly divides another number.
    The returned list should include 1 and the given number n itself.
    The order of the returned list doesn't matter.

    For example:
    - If we call divisors(10), we'll get [1,2,5,10] in return
    - If we call divisors(1), we'll get [1] in return
    """
    # your code here
    
    #empty list for divisors
    divisors = []

    
    #find divisors
    for number in range(1,n+1):
        if n % number == 0:
            divisors.append(number)
    return divisors
            
divisors(10)

def capitalize_or_join_words(sentence):
    """
    If the given sentence starts with *, capitalizes the first and last letters of each word in the sentence,
    and returns the sentence without *.
    Else, joins all the words in the given sentence, separating them with a comma, and returns the result.

    For example:
    - If we call capitalize_or_join_words("*i love python"), we'll get "I LovE PythoN" in return.
    - If we call capitalize_or_join_words("i love python"), we'll get "i,love,python" in return.
    - If we call capitalize_or_join_words("i love    python  "), we'll get "i,love,python" in return.

    Hint(s):
    - The startswith() function checks whether a string starts with a particular character
    - The capitalize() function capitalizes the first letter of a string
    - The upper() function converts all lowercase characters in a string to uppercase
    - The join() function creates a single string from a list of multiple strings
    """
    # your code here
    if sentence.startswith('*'):
        tokens = []
        for word in sentence[1:].split():
            print(word)
            if len(word) < 2:
                tokens.append(word.upper())
                print(tokens)
            else:
                tokens.append(word[0].upper() + word[1:-1] + word[-1].upper())
                print(tokens)
        return ' '.join(tokens)
    return ','.join(sentence.split())

print(capitalize_or_join_words('*i love python'))


def move_zero(lst):
    """
    Given a list of integers, moves all non-zero numbers to the beginning of the list and
    moves all zeros to the end of the list.  This function returns nothing and changes the given list itself.

    For example:
    - After calling move_zero([0,1,0,2,0,3,0,4]), the given list should be [1,2,3,4,0,0,0,0] and the function returns nothing
    - After calling move_zero([0,1,2,0,1]), the given list should be [1,2,1,0,0] and the function returns nothing
    - After calling move_zero([1,2,3,4,5,6,7,8]), the given list should be [1,2,3,4,5,6,7,8] and the function returns nothing
    - After calling move_zero([]), the given list should be [] and the function returns nothing
    """
    # your code here
    zeroslst = []
    nonzerlst = []
    for num in lst:
        if num == 0:
            zeroslst.append(num)
            print(zeroslst)
        else:
            nonzerlst.append(num)
            print(nonzerlst)
       
        lst = nonzerlst + zeroslst 
    return 


            
print(move_zero([0,1,0,2,0,3,0,4]))
        