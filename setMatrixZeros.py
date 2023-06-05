def setZeros(matrix):
    c = 1
    for i in range(len(matrix)):
        if matrix[i][0]==0:
            c = 0
        for j in range(1,len(matrix[0])):
            if matrix[i][j]==0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    for i in range(len(matrix)-1,0,-1):
        for j in range(len(matrix[i])-1,0,-1):
            if matrix[i][0]==0 or matrix[0][j]==0:
                matrix[i][j]=0
    if matrix[0][0]==0:
        for i in range(len(matrix[0])):
            matrix[0][i]=0
    if c==0:
        for i in range(len(matrix)):
            matrix[i][0]=0
print(setZeros([[7, 19, 3],[4, 21, 0]]))
