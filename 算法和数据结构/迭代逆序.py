l1=[1,2,3,4,5,6]
print(len(l1))
l2=[]
for i in range(len(l1)-1,-1,-1):
    l2.append(l1[i])
print(l2)