d=[2,3,4,10,11,12,20,25,30]

print('\n\nDataset contains data are : ',d)
m1=d[2]# randomly pick 2 values from  dataset,d
m2=d[4]


f1,f2=0,0
while True:# for recurcively execution
    k1=[0]*10# 2 cluster array
    k2=[0]*10
    res1,res2=0,0
    f1,f2=m1,m2# storing m1's and m2's previous value 
    c1,c2=0,0 # for counting transition   
    for i in range(0,len(d)):
        p1=abs(m1-d[i])# determing difference from m1 and m2
        p2=abs(m2-d[i])
        if p1>p2: # comparing distance and store lowest value in k2 and k1
            k2[c2]=d[i]
            c2=c2+1
        else:
            k1[c1]=d[i]
            c1=c1+1
    for i in range(0,len(d)): # determinig mean of k1 and k2
        res1=res1+k1[i]
        res2=res2+k2[i]
    res1=res1/c1
    res2=res2/c2
    m1,m2=res1,res2 # updating m1 and m2
    if(f1==m1 and f2==m2): # checking m1 and m2 with its previous value
        break
    
    
print('\n\nCluster k1: ')
for i in range(0,len(k1)):
     if k1[i]==0: # remove extra 0 from k1
         break
     print(k1[i],end=' ')###print in a line
     
     
print('\n\nCluster K2: ')##print new line     
for i in range(0,len(k2)):
     
     if k2[i]==0:# remove extra 0 from k2
        break
     print(k2[i],end=' ')
     
     
print('\n')    
print('The mean m1=',m1,'\nThe mean m2=',m2)