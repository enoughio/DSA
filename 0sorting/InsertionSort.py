
# insertion sort

# it works on the priciple 
# take and element and place it in its correct position
def InsertionSort(arr : []) :

    n = len(arr)

    # for selecting each element in the arrya
    for i in range(0,n) : 

        j = i
        while j > 0 and arr[j] < arr[j-1] : 
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j-=1
        
    return arr


