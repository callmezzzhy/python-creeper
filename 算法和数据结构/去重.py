l=[2,2,3,1,2,74,5,6,6,7,8,9,9]
l1=list(set(l))

l1.sort(key=l.index)
print(l1)
l2={}.fromkeys(l).keys()
print(l2)
l3=[]
[l3.append(x) for x in l if x not in l3]
print(l3)
