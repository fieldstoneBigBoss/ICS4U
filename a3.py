'''
Program:    a3.py
Name:       Jason   Huang
Date:       15/04/2016
Desc:       This program is used to create a new file and put the list which one is already translated to TSV form in the new file
            and read the information then translate it to array form and output it from the new file.

'''

# Initialize the array list that we will use it later.
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

#1
def writeString(filename,string):
    """
    Create a new file and write down something.
    """

    # Create a new file and name it.
    v=open(filename,'w')
    # Write down something in the file.
    v.write(string)
    # Close the file.
    v.close()


#2
def readString(filename):
    """
    Open the new file and read it.
    """

    # Open the new file.
    f=open(filename,'r')
    # Read the information as a string in the new file.
    string=f.read()
    # Close the file.
    f.close()
    # Return the information form the file.
    return string


#3
def writeNum(filename,number):
    """
    Create a new file and input a series of number.
    """

    # Make the numbers as a string.
    i=str(number)
    # Open the file.
    f=open(filename,'w')
    # Input the number.
    f.write(i)
    # Close the file.
    f.close()


#4
def readNum(filename):
    """
    Open the file and read it.
    """

    # Open the file.
    f=open(filename,'r')
    # Read the information as a number.
    number=f.read()
    # Close the file.
    f.close()

    # Text the number is a integer or a float number and return it.
    try:
        return int(number)
    except ValueError:
        return float(number)


#5
def row2TSV(row):
    """
    Translate a row into TSV form and return it.
    """

    # Create an empty list called string.
    string=""

    # Loop through the row.
    for i in range (len(row)):
        # Add "\t" behind each element except the last element.
        string=string+row[i]+"\t"
    # Return the list.
    return string[0:-1]

def array2TSV(array):
    """
    Translate the whole array into TSV form.
    """

    # Create an empty list called string2.
    string2=""

    # Loop through the whole array.
    for a in range (len(array)):
        # Add "\n" behind each list.
        string2=string2+row2TSV(array[a])+"\n"
    # Return string2.
    return string2


#6
def TSV2array(string):
    """
    Translate TSV form into array.
    """

    # Create an empty list called wholeList.
    wholeList=[]

    # Split up each list by "\n".
    list=string[ :-1].split("\n")

    # Loop through list.
    for i in range (len(list)):
        # For each list, split up each element by "\t".
        wholeList=wholeList+[list[i].split("\t")]
    # Return the whole List.
    return wholeList


#7
def writeTSV(filename,array):
    """
    Write an array and translate it into TSV form, then put it in the new file.
    """

    # Create a new file.
    f=open(filename,"w")
    # Translate the array into TSV form and put it into the new file.
    f.write(array2TSV(array))
    # Close the file.
    f.close()


#8
def readTSV(filename):
    """
    Read the information from the file as an array.
    """

    # Open the new file.
    f=open(filename,"r")
    # Translate the information what we read from the file into an array.
    list=TSV2array(f.read())
    # Close the file.
    f.close()
    # Return the list.
    return list




# Input some information into function which shows above so that we can test the program.
print(writeString('afb.txt','sb'))
print(readString('afb.txt'))
print(writeNum('jaman.txt',678))
print(readNum('jaman.txt'))
print(row2TSV(['ICS4U', 'Assignment 1', 'Luke Skywalker', '3+']))
print(array2TSV(database))
print(TSV2array('ICS4U\tAssignment 1\tLuke Skywalker\t3+\nSPH4U\tUnit 1 Test\tYoda\t4+\n'))
print(writeTSV("a3.tsv",database))
print(readTSV("a3.tsv"))