"""
#1
def helloWorld():
    print("Hello world!")
helloWorld()


#2
def greet(x):
    print("Hello",x,"!")
greet("john")


#3
def greet2():
    a=input("What's your name?")
    print("Hello",a,"!")
greet2()


#4
def plus1(num):
    return num+1
plus1(46)


#5
def max3(a,b,c):
    return(max(a,b,c))
max3(1,2,3)


#6
def printN(n):
    for x in range(1,n+1):
        print(x)
printN(9)


#7
def sumN(n):
    return sum(range(1,n+1))
sumN(4)



#8
def strFirst():
    str=input("please input a string:")
    return str[0]
strFirst()


#9
def strHalf():
    str=input("please enter whatever you want!")

    return str[0:int(len(str)//2)]

"""
#10
def guessingGame(x):
    n=0
    while True:
        guess=input("please enter any number that you think:")
        if float(guess)==x:
            n=n+1
            print("Guess",n,". Your guess is right.It's ",x,".")
            return
        else:
            n=n+1
            print("Guess",n,"is wrong !","Try again.")


guessingGame(56)
