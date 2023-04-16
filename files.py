def open_read_file(file):
    """Opens the given file, reads each line and prints to the console. Closes the given file."""
    
    f = open(file, 'r') #open the file in read mode
    print(type(f))
    
    count = 0 #counting the lines of the file
    #reads and prints each line in file, while there is a line to red
    line = f.readline() #reads one line in the file
    
    while line:
        print(line, end = '')
        line = f.readline()
        
        count += 1
    print('')
    print('There are' , count, 'lines in the file')
    
    f.close()

    
def open_read_append_new_file(file1, file2):
    """Opens the first file, and reads all lines into a list. 
    Reverses the lines and appends to the second file. """

lst = []
with open("news.txt", "r") as f: #opens the first file in read mode
    
    #read all lines into a list
    list1 = f.readlines()
    print(list1)
    #reverse the list
    
    list1.reverse()
    print(list1)
    
    #open second file for appending
    fout = open('news.txt', 'a')
    
    #write reversed lines to second file
    fout.writelines(list1)
    
    #close the second file
    fout.close()
    
 #Opens and reads a file, and appends to the same file   
def open_read_append_same_file(file):
    fileA = open(file, 'r')
    
    #read all lines into a list
    list2 = fileA.readlines()
    
    list2.insert(0, '\n')
    list2.insert (0, 'here is some new next line')
    list2.insert (0, '\n')
    
    #append the lines back to the same file
    fileA.writelines(list2)
    fileA.close()
    
def open_read_write_new_file(file3, file4):
    """Opens the first file and reads all the text as a string.
    Copies or writes all text to the second file"""
    
    #open the first file - read only
    with open(file3, 'r') as fin:
        text = fin.read() #reads all lines as a single string
        
    frout = open(file4, 'w') #open second file - write only
    
    frout.write(text) #write single string to second file
    frout.close()
        
    
def main():
    #open_read_file('news.txt')
    #open_read_append_new_file('news.txt', 'news_out.txt')
    #open_read_append_same_file('news.txt')
    open_read_write_new_file('news.txt', 'news_copy.txt')
    
if __name__ == '__main__':
    main()