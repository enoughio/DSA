
# merge sort - divide and merge

def mergeSort(arr): 
    devide(arr, 0, len(arr)-1)

def devide(arr, low, high) : 

    if high == low : 
        return arr

    mid = (low + high)//2

    left = devide(arr, low, mid)
    right = devide(arr, mid+1, high)
    
    return merge(arr, low, mid, mid+1, high)

def merge(arr, a1, a2, b1, b2) : 

    i = a1
    j = b1
    ans = []

    while( i <= a2  and j <= b2 ) : 

        ans = []
        if( arr[i] <= arr[j] ) : 
            ans.append(arr[i])
            i+=1
        else : 
            ans.append(arr[j])
            j+=1
    
    while i <= a2 :
        ans.append(arr[i])
        i+=1
    
    while j <= b2 :
        ans.append(arr[j])
        j+=1


    return ans
    # or we can also copy the ans array to the orignal array    