def isOdd(list):
    if list==[]:
        return False
    elif (list[0]%2)==1:
        return
    else:
        return isOdd(list[1:])


def fatorial(x):
    x=x



def loafLength(loaf):

    if loaf ==[]:
        return 0


    loaf.pop()
    return 1+loafLength(loaf)

print(loafLength([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))


def  laugh(n):
    if n<=0:
        return " "
    return "HA "+laugh(n-1)

print(laugh (4))


def sum(list):


    if list==[]:
        return 0
    return list[0]+sum(list[1: ])

print(sum([1,2,3,4,5]))

def allEqual(x):
    if len(x)==1:
        return True
    return x[0]==x[1] and allEqual(x[1: ])


def countDown(n):
    if n==0:
        return 0
    print (n)
    countDown(n-1)
countDown(5)

"""
def countUp(n):


    return n,countUp(n-(n-1))
"""


import os
root=r"C:\Users\jason\PycharmProjects\ICS4U"
file=os.listdir(root)
print(file)
print(file[0])
filePath =os.path.join(root,file[1])
print(filePath)

print( os.path.isdir(filePath))




