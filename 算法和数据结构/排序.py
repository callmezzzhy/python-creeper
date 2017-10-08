def ssort(l):
    if not l :
        return []
    else:
        start=l[0]
        lower=ssort([x for x in l[1:] if x<l[0]])
        upper=ssort([x for x in l[1:] if x>l[0]])
        new=[start]
        return lower+new+upper
l=[1,4,6,8,5,3,]
print(ssort(l))