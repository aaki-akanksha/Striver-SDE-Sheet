def maxSubarraySum(arr, n) :
    maxi = -10**7
    sum = 0
    for i in range(n):
        sum += arr[i]
        if sum>maxi:
            maxi = sum
        if sum<0:
            sum = 0
    return maxi if maxi>0 else 0
print(maxSubarraySum([1, 2, 7, -4, 3, 2, -10, 9, 1],9))
