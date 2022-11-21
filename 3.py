valid_nos=[0,1,2,5,6,8,9]
input1=int(input())
i=1
found=0

while found!=input1:
    if i in valid_nos:
        found+=1
    else:
        f1=1
        for j in str(i):
            if int(j) not in valid_nos:
                f1=0
                break
        if f1==1:
            found+=1
    i+=1
print(i-1)
