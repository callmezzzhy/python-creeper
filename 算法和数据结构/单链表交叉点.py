class listNode(object):
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
t1=listNode(1,listNode(2,listNode(3,listNode(4,listNode(5,listNode(6))))))
t2=listNode(1,listNode(2,listNode(3,listNode(5,listNode(6)))))
def jiaocha(l1,l2):
    l3=l1
    l4=l2
    if l1==None and l2==None:
        return 0
    lenth1,lenth2=0,0
    while l1.next:
        lenth1+=1
        l1=l1.next
    while l2.next:
        lenth2+=1
        l2=l2.next
    l=[]
    while l3 and l4 :
        if l3.data==l4.data:
            l.append(l3.data)
            l3=l3.next
            l4=l4.next
        else:
            l3=l3.next
            l4=l4.next
    return l

a=jiaocha(t1,t2)
print(a)