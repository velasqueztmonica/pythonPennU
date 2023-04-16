#creating a dictionary for each student

billy = {
    'name': 'Billy',
    'grades': [100,80,67,100,89],
    'attendance': [True, True, True, True, True]
}


sarah = {
    'name': 'Sarah',
    'grades': [0,99,0,100,0],
    'attendance': [True, False, True, False, True]
}

ben = {
    'name': 'Ben',
    'grades': [60,82,71,92,100],
    'attendance': [False, False, False, False, False]
}

#dictionary of students by id, remember it is giving a value from above
students ={
    '1': billy,
    '2': sarah,
    '3': ben
}

#get the number of students

print(len(students))

#get all students id
print(students.keys())

#iterate over the dictionary to get the keys
for k in students:
    print('key:', k)
    
# get billy's attendance
billy = students['1']
print(billy['attendance'])

#get Sarah's grades
sarah = students['2']
print(sarah['grades'])

#other way
sarah = students.get('2')
print(sarah.get('grades'))

ben = students.get('3')
items = ben.items() # sequence of tuples
for key, val in items:
    print(key, val)
    
#Get the average of student grade for all assignment
grades =[]
items2 = students.items()
print(items2)
for key, val in items2: # key is student id, the val is the studen
    for g in val['grades']: #val is the student
        grades.append(g)
print(sum(grades) / len(grades))

#another way

grades_conc = []
items3 = students.items()
for key, val in items3:
    grades_conc += val['grades']

print(sum(grades_conc) / len(grades_conc))