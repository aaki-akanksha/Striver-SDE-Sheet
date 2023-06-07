def printPascal(n):
    r = []
    for i in range(n):
        r.append([1]*(i+1))
        for j in range(1,(i//2)+1):
            r[i][j]=r[i][i-j]=r[i-1][j-1]+r[i-1][j]
    return r
print(printPascal(10))
