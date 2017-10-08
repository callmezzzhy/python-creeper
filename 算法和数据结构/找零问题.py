def changge(money):
    mag=[100.50,20,10,5,1,0.5,0.1]
    moneys=int(money*10)
    temp=[]
    loop=True
    while loop:
        if moneys==0:
            loop=False
        else:
            for row in mag:
                jie=row*10
                if jie>=10:
                    tmp='元'
                else:
                    tmp='角'
                if moneys>jie:
                    m=moneys//jie
                    moneys=moneys%jie
                    if jie>=10:
                        temstr=str(jie//10)+tmp+str(m)+'张'
                    else:
                        temstr=str(jie//10)+tmp+str(m)+'张'
                    temp.append(temstr)
    return temp
l=changge(83)
print(l)