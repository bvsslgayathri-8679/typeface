n=int(input())
res=''
while n>=3:
    res+=str(n%3)
    n=n//3
res+=str(n)

print(res[::-1])