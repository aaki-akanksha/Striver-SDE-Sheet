def sort012(arr, n) :
    l = m = 0
    h = n-1
    while m<=h:
        if arr[m]==0:
            arr[l],arr[m]=arr[m],arr[l]
            l+=1
            m+=1
        elif arr[m]==1:
            m+=1
        else:
            arr[m],arr[h]=arr[h],arr[m]
            h-=1
 print(sort012([2,1,0,0,2,1,0],7))
