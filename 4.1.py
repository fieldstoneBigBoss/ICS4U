def linearSearch(array,value):
    for i in range(len(array)):
        if array[i]==value:
            return i

    return None

def binarySearch(array,value):
    L=0
    R=len(array)-1
    while L<=R:
        m=(L+R)//2
        if array[m]==value:
            return m
        if array[m]<=value:
            L=m+1
        if array[m]>=value:
            R=m-1
    return None

array=[4,8,15,16,23,42]
print(binarySearch(array,23))


