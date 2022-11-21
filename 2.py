str1=input()
str2=input()
result=0
ch=str2[-1]
for i in str1:
    if i==ch:
        result+=1

print(result)