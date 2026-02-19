
# bubble swap 


def bubbleSwap(arr) : 

    n = len(arr)

    # from n-1 to 1 
    for i in range(n-1, -1 , -1) :   
        
        # flag
        didSwap = False

        # form 0 - i-1
        # becasue we are comparing j and j+1 so last elem should never ve 
        for j in range(0, i) : 

            # adjecent swap
            # bring th max elem to the top
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                didSwap = True

        if didSwap == False : 
            break
    
    return arr

