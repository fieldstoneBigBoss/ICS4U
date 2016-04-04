#1
def printChars(string):
    print("\n".join(string))
printChars("sbjohn")


#2
def emailDomain(string):
    a=string.split('@')
    return a[1]
print(emailDomain("myname@domain.com"))


#3
def printSorted(string1,string2):
    if string1<string2:
        print(string1)
        print(string2)
    else:
        print(string2)
        print(string1)
printSorted("sbjohn","joinsb")


#4
def compareLength(string1,string2):
    return len(string1)==len(string2)
compareLength("sbjohn","johnsb")



#4