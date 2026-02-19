# selection sort code 


def selectionSort(arr) : 

    n = len(arr)
    
    # runs 0 - n-2
    # leaving the last elemtnt in its place
    for i in range(0, n-1) : 

        # runs i-n-1
        mini = i
        for j in range(j, n) : 
            
            # find minimum in the remaining array
            if arr[j] < arr[mini] :
                mini = j

        # swap
        arr[mini], arr[i] =  arr[i], arr[mini]

    return arr