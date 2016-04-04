def isOdd(x):
    return x%2
print(isOdd(5))



def canDiv57(x):
    return x%5==0 and x%7==0
print(canDiv57(35))zzz

"""
def thirdDigit7(x,d):
    return x // 10**(d-1) % 10
print(thirdDigit7(7738755475325805646754554,5))
"""


def getDigit(x,n):
    return x // 10**(n) % 10
print(getDigit(2011,2))
def fsdf(x):
    a=getDigit(x,3)
    b=getDigit(x,2)
    c=getDigit(x,1)
    d=getDigit(x,0)

    print(a+b+c+d)
    print(d,c,b,a,sep="")
    print(d,a,b,c,sep="")
    print(a,c,b,d,sep="")
    return
fsdf(2011)

def