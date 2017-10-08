l2=[3,4,6,7,8,9,5,6]
l1=[1,2,4,5]
def hebin(l1,l2):
    l3=[]
    if len(l1)==0 and len(l2)==0:
        return 0
    while len(l1) > 0 and len(l2) > 0:
            if l1[0]<l2[0]:
                l3.append(l1[0])
                #print(l3)
                del l1[0]
            else:
                l3.append(l2[0])
                del l2[0]
    l3.extend(l1)
    l3.extend(l2)
    return l3

l=hebin(l1,l2)
print(l)
