r=int(input())
c=int(input())
l=[]
for i in range(r):
    t=list(map(int,input().split()))
    l.append(t)   
l1=[]
l2=[]
for i in range(r):
    for j in range(c):
        if l[i][j]==0:
            l1.append(i)
            l2.append(j)
l2.sort()
t=[(l1[0],l2[0]),(l1[0],l2[-1]),(l1[-1],l2[0]),(l1[-1],l2[-1])]
print(t)