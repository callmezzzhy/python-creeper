def right(ll,spl):
    r=ll.rfind(spl)
    while r!=0 and r==len(ll)-1:
        ll=ll[:r]
        r=ll.rfind(spl)
    return l
def left(ll,spl):
    s=ll.find(spl)
    while s==0:
        ll=ll[1:]
        s=ll.find(spl)
    return ll

l='   323  '
l1=right(l,' ')
print(l1)
l2=left(l,' ')
print(l2)


