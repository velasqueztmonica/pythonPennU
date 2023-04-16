#Tuples Exercise
#Create a max_ and min_ that returns a tuple containing the max and min of a given list
#First create the max_ and min_ function itself

def max_and_min_(lst):
    """Return max and min of a list"""
    return (max(lst), min(lst))

def main():
    list1 = [10, -1,-34, 56]
    outputNum = max_and_min_(list1)
    
    #first, take a look at the type
    print(type(outputNum))
    
    max_num = outputNum[0]
    min_num = outputNum[1]
    
    print(max_num,min_num)
    
    
if __name__ == '__main__':
    main()