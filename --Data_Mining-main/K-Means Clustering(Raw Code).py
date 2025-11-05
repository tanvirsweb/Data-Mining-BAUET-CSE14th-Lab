d=[2,3,4,10,11,12,20,25,30]
print('\n\nDataset Contains Data are: ',d)
m1=d[2]
m2=d[4]
f1,f2=0,0
while True:
    k1=[0]*10
    k2=[0]*10
    res1,res2=0,0
    f1,f2=m1,m2
    c1,c2=0,0
    for i in range(0, len(d)):
        p1=abs(m1-d[i])
        p2=abs(m2-d[i])
        if p1>p2:
            k2[c2]=d[i]
            c2=c2+1
        else:
            k1[c1]=d[i]
            c1=c1+1

    for i in range(0,len(d)):
        res1=res1+k1[i]
        res2=res2+k2[i]
    res1=int(res1/c1)
    res2=int(res2/c2)

    m1,m2= res1,res2
    if(f1==m1 and f2==m2):
        break
        
print('\n\n CLuster k1: ')
for i in range(0, len(k1)):
    if (k1[i]==0):
       break
    print(k1[i],end=' ')
print('\n\n CLuster k2: ')
for i in range(0, len(k2)):
    if (k2[i]==0):
       break
    print(k2[i],end=' ')