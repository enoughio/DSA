        

def en(s) : 
    n = len(s)

    i = 1
    ch = s[0]
    cnt = 1
    while i < n : 
        if s[i] == ch : 
            cnt +=1
        else : 
            if cnt == 1 : 
                ans = ch + ans 
            else : 
                ans = f"{cnt}[{ch}]" + ans
            ch = s[i]
            cnt = 1
    return ans 


print(en("hello"))



# ------------------- 

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        
        for st in strs : 
            n = len(st)
            encoded = encoded + f"{n}#{st}"
        
        return encoded


    def decode(self, s: str) -> List[str]:
        
        print(s)
        n = len(s)
        i = 0
        ans = []

        while i < n :
            
            cnt = ''
            while s and s[i] != '#' : 
                cnt = cnt + s[i]
                i+=1
            
            i+=1
            cnt = int(cnt)

            block = ""
            for c in range(cnt) : 
                block =  block + s[i]
                i+=1
            
            ans.append(block)

        return ans


# ----- solved : range sum querry 1d -----

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.presum = {}


        self.presum[-1] = 0
        sum = self.nums[0]
        self.presum[0] = sum
        for i in range(1, len(self.nums)) : 
            sum = sum + self.nums[i]
            self.presum[i] = sum

    def sumRange(self, left: int, right: int) -> int:

        st = self.presum[left-1]
        lg = self.presum[right]

        return lg - st 


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)



# ------------- solved : range sum querry in 2d martrix  ----


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix 
        self.presum = []

        rows = len(self.matrix)
        cols = len(self.matrix[0])

        for i in range(rows) : 
            
            sum = matrix[i][0]
            presum = [0]*cols
            presum[0] = matrix[i][0]

            for j in range(1, cols) : 
                sum = sum + matrix[i][j]
                presum[j] = sum

            self.presum.append(presum)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        total = 0
        for i in range(row1, row2+1) : 
            if col1 == 0 : 
                total += self.presum[i][col2]
            else : 
                total += self.presum[i][col2] - self.presum[i][col1-1]

        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)