class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []   # to store answer
        arr = [0]*n  # array of size n
        i = 0
        self.rec(i, n, arr, ans)

        return ans
    
    def rec(self, i: int, n : int, arr: list, ans : list ):

        #base case
        if i == n :                             # if the length of string is equal to n
            st  = str(arr.copy())               # then append it to answer
            ans.append(st)
            return

        if i == 0 :                         # if it is the 0th index then we allow both 0 and 1
            arr[0] = 0
            self.rec(i+1, n, arr, ans)
        elif i != 0 and arr[i-1] != 0 :         # if the last digit is not 0
            arr[i] = 0                          # then add a 0 after it
            self.rec(i+1, n, arr, ans)
        
        arr[i] = 1                              # add 1 at the end in all cases
        self.rec(i+1, n, arr, ans)




## for an list of stings 

class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []   # to store answer
        self.rec(0, n, '', ans)

        return ans
    
    def rec(self, i: int, n : int, arr: str, ans : list ):

        #base case
        if i == n :                             # if the length of string is equal to n
            ans.append(arr)              # then append it to answer
            return

        if i == 0 :                         # if it is the 0th index then we allow both 0 and 1
            self.rec(i+1, n, arr + '0', ans)
        elif arr[-1] != '0' :         # if the last digit is not 0
            self.rec(i+1, n, arr + '0' , ans)   # then add a 0 after it
        
                                    # add 1 at the end in all cases
        self.rec(i+1, n, arr +  '1', ans)





