'''
Program:    a4.py
Name:       Jason Huang
Date:       01/05/2016
Desc:       This program is used to make an unsorted array in a increasing order.
'''

# Import required libraries.
import copy, random, timeit

def funcTimer(func):
    '''
    Time the specified function, running it 100 times with a random array.
    '''
    
    # Create the strings to be run.
    arrayStr = 'array = [random.randint(0,1000) for i in range(200)]'
    funcStr = '{}; a4.{}(array)'.format(arrayStr, func.__name__)

    # Run the test and return the result.
    return timeit.timeit(funcStr, setup='import random, a4', number=100)

#1
def swap(array,a,b):
    '''
    Swap two elements in an array.
    There is no return - this function modifies the input array directly.
    '''

    #Exchange array[a] and array[b]
    xOriginal=array[a]
    array[a]=array[b]
    array[b]=xOriginal

    #Return the final array.
    return array



#2
def findMin(array):
    '''
    Return the index of the minimum value in the array.
    '''

    #Loop through the array.
    for i in range (len(array)):

        #Find the the minimum element.
        if min(array)==array[i]:

            #return the location of the minimun element.
            return i



#3
def sort(array):
    '''
    Sort an array from lowest to highest using #NAME YOUR SORTING METHOD HERE#.
    '''

    # Make a copy of array, so that the input array isn't modified.
    array = copy.deepcopy(array)

    ### PROGRAM THE REST OF YOUR SORTING FUNCTION HERE ###

    #Loop through the array.
    for i in range (len(array)):

        #Exchang the first element and the minimun one for each special list.
        swap(array,i,findMin(array[i: ])+i)

    # Return the sorted array.
    return array


#Check each function and print the result out.
print(swap([1,2,3,4,5,6],0,1))
print(findMin([1,2,3,4,5,6]))
print(sort([10,9,8,7,6,5,4,3,2,1]))



if __name__=="__main__":
    ### PUT ANY EXTRA CODE (TESTING, ETC) HERE ###
    # Create an array of random numbers.
    array = [random.randint(0,100) for i in range(10)]

    # Print the array, the sorted array, and the elapsed time for 100 tests.
    print(array)
    print(sort(array))
    print(funcTimer(sort))
