
# merge sort - divide and merge

def mergeSort(arr): 


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

        if( arr[i] >= arr[j] ) : 
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
        