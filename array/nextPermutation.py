def nextPermutation(permutation, n):
    idx = -1
    for i in range(n-2,-1,-1):
        if permutation[i]<permutation[i+1]:
            idx = i
            break
    if idx==-1:
        permutation.reverse()
    else:
        for i in range(n-1,idx,-1):
            if permutation[i]>permutation[idx]:
                permutation[i],permutation[idx] = permutation[idx],permutation[i]
                break
        permutation[idx+1:] = permutation[idx+1:][::-1]
    return permutation
print(nextPermutation([1,2,3,4],4))
