"""
#1
def diff(x,y):
    return float(x)-float(y)
diff(0.3,0.1+0.2)
"""

#2
def isEqual(x,y):

       return x-y<=0.1**10 or y-x<=0.1**10
print(isEqual(0.1+0.2,0.3))