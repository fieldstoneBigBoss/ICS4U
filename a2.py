'''
Program:    a2.py
Name:       Jason   Huang
Date:       04/04/2016
Desc:       This programm is about how to get the average grades of the students or the classes.
'''

# Initialize the database of student grades
database = [
    ['ICS4U', 'Assignment 1', 'Luke Skywalker', '3+'],
    ['ICS4U', 'Assignment 1', 'Han Solo', '4-'],
    ['SPH3U', 'Unit 1 Test', 'Leia Organa', '4'],
    ['SPH3U', 'Unit 1 Test', 'Luke Skywalker', '3-'],
    ['SPH4U', 'Unit 1 Test', 'Yoda', '4+'],
    ['SPH4U', 'Unit 1 Test', 'Anakin Skywalker', '3'],
    ['MHF4U', 'Unit 1 Test', 'Boba Fett', '2+'],
    ['MHF4U', 'Unit 1 Test', 'Kylo Ren', '3'],
    ['MHF4U', 'Unit 1 Test', 'Chewbacca', '4']

    ]

def tfInput(string):
    ''' Prompt the user for a yes/no question and return True/False '''
    # Display the question and return an answer
    answer = input(string)
    return answer[0].lower() == 'y'


# ICS4U:
# PUT ALL OF YOUR FUNCTIONS HERE
#1
def level2Percent(level):
            if level=="4+":
                return 100
            elif level=="4":
                return 94
            elif level=="4-":
                return 86
            elif level=="3+":
                return 79
            elif level=="3":
                return 76
            elif level=="3-":
                return 72
            elif level=="2+":
                return 69
            elif level=="2":
                return 66
            elif level=="2-":
                return 62
            elif level=="1+":
                return 59
            elif level=="1":
                return 56
            elif level=="1-":
                return 52
            elif level=="<1" or "< 1":
                return 40




#2
def percent2Level(percent):
    if percent in range(95,101):
        return "4+"
    if percent in range(87,95):
        return "4"
    if percent in range(80,87):
        return "4-"
    if percent in range(77,80):
        return "3+"
    if percent in range(73,77):
        return "3"
    if percent in range(70,73):
        return "3-"
    if percent in range(67,70):
        return "2+"
    if percent in range(63,67):
        return "2"
    if percent in range(60,63):
        return "2-"
    if percent in range(57,60):
        return "1+"
    if percent in range(53,57):
        return "1"
    if percent in range(50,53):
        return "1-"
    if percent in range(0,50):
        return "<1" or "< 1"




#3
def stringCompare(string1,string2):
    return string1.lower().strip()==string2.lower().strip()




#4
def addGrade(datebase,course,assignment,student,grade):
    return database+[[course,assignment,student,grade]]




#5
def inputGrades(database):
    course=input("What is the name of the class?: ")
    assignment=input("What is the name of the assignment/test?:")
    while True:
        student=input("Student name:")
        grade=input("Level:")
        database=database+[[course,assignment,student,grade]]
        response=tfInput("Would you like to input another grade?")

        if response==True:
            pass
        elif response==False:
            break
    return database




#6
def studentAverage(database,student):
    grades=[ ]
    percentGrades=[]
    sum=0
    for entry in range(len(database)):
        if stringCompare(database[entry][2],student)==True:
            grades.append(database[entry][3])

    for i in range(len(grades)):
        percentGrades.append(level2Percent(grades[i]))

    for a in range(len(percentGrades)):
        sum=sum+percentGrades[a]


    return sum/ len(percentGrades)




#7
def courseAverage(database,course):
    grades=[ ]
    percentGrades=[]
    sum=0
    for entry in range(len(database)):
        if stringCompare(database[entry][0],course)==True:
            grades.append(database[entry][3])

    for i in range(len(grades)):
        percentGrades.append(level2Percent(grades[i]))

    for a in range(len(percentGrades)):
        sum=sum+percentGrades[a]


    return sum/ len(percentGrades)






if __name__=="__main__":
    pass
    # ICS4U:
    # PUT ANY EXTRA CODE (TESTING, ETC) HERE
    print(level2Percent("3"))
    print(percent2Level(77))
    print(stringCompare(" student","STUDeNT     "))
    print (addGrade(database,"SPH4U","ODS","JOHN","4"))
    print(inputGrades(database))
    print(studentAverage(database,"Luke Skywalker"))
    print(courseAverage(database,"ICS4U"))