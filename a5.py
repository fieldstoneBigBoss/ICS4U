'''
Program:    a5.py
Name:       Jason Huang
Date:       09/06/2016
Desc:       This is a program about recursive function. The function will loop again and again until get the right
            answer we want.
'''

import os

### PROGRAM YOUR FUNCTIONS HERE! ###


#1
def power(x,n):
    '''
    This function is used to get the answer x power of n.
    '''

    #If power is equal or small than zero, then stop the function.
    if n==0:
        return 1

    #Loop the function and get the answer.
    return x*power(x,n-1)



#2
def morePower(x,n):
    '''
    This function can calculate x power of n more efficiently.
    '''

    #When n equal to 0 then stop the function.
    if n==0:
        return 1

    #If n is even number then run this piece.
    if n%2==0:
        #loop the function again.
        return morePower(x,n//2)*morePower(x,n//2)

    #If n is odd number then run this piece.
    if n%2==1:
        #loop the function.
        return x*morePower(x,n//2)*morePower(x,n//2)



#3
def GCF(a,b):
    '''
    This function is used to find the greatest common factor of any two numbers.
    '''

    #If a equal to 0, then the answer is b.
    if a==0:
        #Return the answer.
        return b

    #If b equalto 0, then the answer is a.
    if b==0:
        #Return the answer.
        return a

    #Get the greatest common factor of a and b.
    return GCF(b,a%b)



#4
def isPalindrome(string):
    '''
    This function checks whether a string is a palindrome.
    '''

    #If the length of string is equal to 0 or 1 then get the answer.
    if len(string)==1 or len(string)==0:
        #Return the answer.
        return True

    #Find the function whether a palindrome or not, and return the answer.
    return string[0]==string[-1] and isPalindrome(string[1:-1])



#5
def printFiles(root):
    '''
    This function prints all files in given folder.
    '''

    #Create a list of all files and folder at the given path.
    originalFiles=os.listdir(root)

    #Loop through the list which name 'originalFiles'.
    for i in range (len(originalFiles)):
        #Find the object is a folder or file.
        tf=os.path.isdir(os.path.join(root,originalFiles[i]))

        #If it is a folder, then run this piece.
        if tf==True:
            #Recurring the function and print out the path of the final file.
            path=os.path.join(root,originalFiles[i])
            #Print the path.
            printFiles(path)

        #If it is a file, then run this piece.
        if tf==False:
            #Get the path of the file.
            path=os.path.join(root,originalFiles[i])
            #Print the path of the file.
            print (path)






if __name__=="__main__":
    ### PUT ANY EXTRA CODE (TESTING, ETC) HERE ###
    print(power(5,3))
    print(morePower(5,4))
    print(GCF(54,15))
    print(isPalindrome("johnnhoj"))
    print(printFiles(r"C:\Users\jason\PycharmProjects\ICS4U"))
    pass



