def numeric_to_letter_grade(numericalGrade):
    #numericalGrade = int(input("Enter your grade: "))

    if numericalGrade >= 90 :
        print("A")
    elif numericalGrade >= 80 :
        print("B")
    elif numericalGrade >= 70 :
        print("C")
    elif numericalGrade >= 60 :
        print("D")
    else :
        print("F")
        
#Call the numeric_to_letter_grade function
numericalGrade = int(input("Enter your grade: "))
numeric_to_letter_grade(numericalGrade)