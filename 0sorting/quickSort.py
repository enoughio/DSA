
# pick up a pivot and place it in its right place
# in the process everything on the left will be smaller then/equal to the pivot, 
# and everything to the left will be greater then pivot


def QuickSort(arr, low, high) : 

    if low >= high : 
        return arr

    partIdx = partition(arr, low, high)

    quickSort(arr, low, partIdx-1)
    quickSort(arr, partIdx+1, high)

def partition(arr, low, high) : 

    i = low
    j = high
    pivot = low

    while(i < j) : 

        while i < high and arr[i] <= arr[pivot] : 
            i+=1
        
        while j > low and arr[j] > arr[pivot] :
            j-=1

        if( i < j) :
            arr[i], arr[j] = arr[j], arr[i]


     
    arr[j], arr[pivot] = arr[pivot], arr[j]
    return j