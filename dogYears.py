import traceback
#Defining the function
def calculator():
    
    #Defining the input
    age = input("Input dog years: ")
    
    try:
        dog_age = float(age)
        if dog_age < 0:
           print('This is a negative number; invalid input')
        elif 0 < dog_age <=1:
            human_age = dog_age * 15;
        elif 1 < dog_age <=2:
            human_age = dog_age * 12;
        elif 2 < dog_age <=3:
            human_age = dog_age * 9.3;
        elif 3 < dog_age <=4:
            human_age = dog_age * 8;
        elif 4 < dog_age <=5:
            human_age = dog_age * 7.2;
        else:
            human_age = (5 * 7.2) + (dog_age - 5) * 7;
        print("The given dog age", dog_age, "is ", round(human_age,2), "in human years.")
    except:
        print(age, "is an invalid age.")
        print(traceback.format_exc())
        
#Calling the function
calculator()