def word_count(sentence):
    
    sentence = sentence.strip() #removes whitespace 
    
    num_spaces = count_instance_of_str(sentence, " ")
    
    word_count = num_spaces + 1
    
    return word_count

def count_instance_of_str(string1, string2):
    """Counts characters in string1 that are also in string2"""
    
    count = 0 
    #for each char in string1, check if it's in string2
    
    for char in string1:
        if char in string2:
            count += 1
    return count

def main():
    while 1 == 1:
        input_string = input("Enter a string: ")
        if  input_string == '-1':
            break
        
        #print(vowel_count(input_string), 'vowels in', input_string)
        print(word_count(input_string), 'words in', input_string)

if __name__ == '__main__':
    main()