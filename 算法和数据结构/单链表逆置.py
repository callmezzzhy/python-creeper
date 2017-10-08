class Node(object):
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
t1=Node(1,Node(2,Node(3,Node(4,Node(5,Node(6))))))
def rever(l):
    pre=l
    cur=l.next
    pre.next=None
    while cur:
        tmp=cur.next
        cur.next=pre
        pre=cur
        cur=tmp
    return pre
root=rever(t1)
while root:
    print(root.data)
    root = root.next
