'''
Program:    a5.py
Name:       Jason Huang
Date:       
Desc:       
'''

import os

### PROGRAM YOUR FUNCTIONS HERE! ###


#1
def power(x,n):
    if n==0:
        return 1
    return x*power(x,n-1)

print(power(5,3))


#2
def morePower(x,n):
    if n==0:
        return 1
    if n%2==0:
        return morePower(x,n//2)*morePower(x,n//2)
    if n%2==1:
        return x*morePower(x,n//2)*morePower(x,n//2)

print(morePower(5,4))


#3
def GCF(a,b):
    if a==0:
        return b
    if b==0:
        return a
    return GCF(b,a%b)

print(GCF(54,15))


#4
def isPalindrome(string):
    if len(string)==1 or len(string)==0:
        return True
    return string[0]==string[-1] and isPalindrome(string[1:-1])

print(isPalindrome("johnnhoj"))











if __name__=="__main__":
    ### PUT ANY EXTRA CODE (TESTING, ETC) HERE ###
    pass



