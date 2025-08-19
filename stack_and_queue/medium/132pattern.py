def find132pattern(nums) : 

    st = []
    third = float('-inf')

    # treverse array form right to left
    for i in reversed(nums) : 

        # if the current number is smaller then third then we found the 132 pattern 
        if i < third : 
            return True 

        # pop element from the stack which are smaller then or equal to the current number 
        while st and st[-1] < i : 
            third = st.pop()   #store it as the third number

        # push the current number into the stack 
        st.append(i) 

    # if reversed complete then, 132 pattern is not found  
    return False  



print(find132pattern([-1,2,3,4,2]))