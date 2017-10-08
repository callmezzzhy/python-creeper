import math

def erfenfa(l,num):
    if len(l)<0:
        return None
    else:
        low=0
        high=len(l)-1
        while low<high:
            mid=math.floor((low+high)/2)
            if l[mid]<num:
                low=mid+1
            elif l[mid]>num:
                high=mid
            else:
                return mid
        return low if l[low]==num else None
l=['1','2','3','4','5','6','7']
a=erfenfa(l,'8')
print(a)