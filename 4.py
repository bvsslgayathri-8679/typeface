def FindSubMatrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
 
    temp = []
    for i in range(rows):
        temp1 = []
        for j in range(cols):
            if i == 0 or j == 0:
                temp1 += matrix[i][j],
            else:
                temp1 += 0,
        temp += temp1,

    for i in range(1, rows):
        for j in range(1, cols):
            if (matrix[i][j] == 0):
                temp[i][j] = min(temp[i][j-1], temp[i-1][j],temp[i-1][j-1]) + 1
            else:
                temp[i][j] = 0

    max_val = temp[0][0]
    maxi = 0
    maxj = 0
    for i in range(rows):
        for j in range(cols):
            if (max_val < temp[i][j]):
                max_val = temp[i][j]
                maxi = i
                maxj = j
 
    print(tuple((maxi-max_val,maxj)),',',tuple((maxi-max_val,maxj+max_val)),',',tuple((maxi,maxj)),',',tuple((maxi,maxj+max_val))) 
 
n=int(input())
matrix=[list(map(int,input().split())) for i in range(n)]
 
FindSubMatrix(matrix)
