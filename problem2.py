s1=input()
s2=input()
key=s2[-1]
c=0
for i in s1:
    if i==key:
        c+=1
print(c)