def myFun(a,b):
    print('a:',a,'b:',b,sep='\t')
    if a<=0:
        return
    elif b>a:
        myFun(a,b-1)
    else:
        myFun(a-1,b)
myFun(2,3)