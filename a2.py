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
    """
    Translate the level into percentage.
    """

    # Make each level  equal to a exact number.
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
    """
    Make the grades into Level form.
    """

    #Let the number equal to a level.
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
    """
    Compare string1 and string2.
    """

    #return the answer of the compare result.
    return string1.lower().strip()==string2.lower().strip()




#4
def addGrade(datebase,course,assignment,student,grade):
    """
    Add a new list into database.
    """

    #Return the new line.
    return database+[[course,assignment,student,grade]]




#5
def inputGrades(database):
    """
    Get the information from the user and add them to database as a new line.
    """

    #Asking the information about the course and assignment.
    course=input("What is the name of the class?: ")
    assignment=input("What is the name of the assignment/test?:")

    #Loop ask question from the user.
    while True:
        student=input("Student name:")
        grade=input("Level:")
        database=database+[[course,assignment,student,grade]]

        #Asking the user whether loop or not.
        response=tfInput("Would you like to input another grade?")
        if response==True:
            pass
        elif response==False:
            break

    #return the answer.
    return database




#6
def studentAverage(database,student):
    """
    Get the average grades of the student.
    """

    #Creat the new name.
    grades=[ ]
    percentGrades=[]
    sum=0

    #Loop through the database.
    for entry in range(len(database)):

        #Whether the name is same as the student.
        if stringCompare(database[entry][2],student)==True:
            #Add the score into grades.
            grades.append(database[entry][3])

    #Loop through the grades.
    for i in range(len(grades)):
        #Translating the score into percentage.
        percentGrades.append(level2Percent(grades[i]))

    #Loop through the percentGrades.
    for a in range(len(percentGrades)):
        #Get the sum of the percentGrades.
        sum=sum+percentGrades[a]

    #Return the average grades.
    return sum/ len(percentGrades)




#7
def courseAverage(database,course):
    """
    Calculate average grades of the course and return the answers.
    """

    #Creat the new name.
    grades=[ ]
    percentGrades=[]
    sum=0

    #Loop through the database.
    for entry in range(len(database)):

        #Compare the course.
        if stringCompare(database[entry][0],course)==True:

            #If the course is same as our type then take out the score.
            grades.append(database[entry][3])

    #Loop through the grades.
    for i in range(len(grades)):

        #Make the grades translate to percentage.
        percentGrades.append(level2Percent(grades[i]))

    #Loop through the grades which is percentage.
    for a in range(len(percentGrades)):

        #Get the sum of the percentGrades.
        sum=sum+percentGrades[a]

    #Return the result.
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