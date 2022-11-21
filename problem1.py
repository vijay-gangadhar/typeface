n  = int(input())
ans = ""
while n>=3:
    ans+=str(n%3)
    n = n//3
ans = ans[::-1]
ans =  str(n) +ans
print(ans)
