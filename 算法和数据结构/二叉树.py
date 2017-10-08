class Node(object):
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
t1=Node(1,Node(3,Node(7,Node(0)),Node(6,Node(8,Node(7)))),Node(2,Node(5),Node(4)))
t2=Node(1,Node(3,Node(7,Node(0)),Node(6,Node(8))),Node(2,Node(5),Node(4)))
#print(t1)
#层次遍历
def listnode(t):
    stack=[t]
    #stacks=[]
    while stack:
        current=stack.pop(0)
        print(current.data)
        if current.left:
            stack.append(current.left)
            #stacks.append(current.left)
        if current.right:
            stack.append(current.right)
            #stacks.append(current.right)
        #print(stacks)
    #return stacks
#listnode(t1)

#深度遍历
def deeplist(l):
    if not l:
        return None
    else:
        print(l.data)
        deeplist(l.left)
        deeplist(l.right)

#deeplist(t1)
import math
#最大树深
def maxtree(l):
    if not l:
        return 0
    return max(maxtree(l.left),maxtree(l.right))+1
#树深
def maxdepth(l):
    if not l:
        return 0
    stack=[l]
    i,j=1,1
    stacks=[l]
    #print(stacks)
    while stack:
        try:
            current=stack.pop(0)
            if current.left:
                i+=1
                stack.append(current.left)
        except:
            return i
    while stacks:
        try:
            currents=stacks.pop(0)
            if currents.right:
                j+=1
                stacks.append(currents.right)

        except:
            return j
    return max(i,j)


#print(maxdepth(t1))

#树相同
def issame(l1,l2):
    if l1==None and l2==None:
        return True
    elif l1==None or l2==None:
        return False
    elif l1.data==l2.data:
        return issame(l1.left,l2.left) and issame(l1.right,l2.right)
    else:
        return False
print(issame(t1,t2))

