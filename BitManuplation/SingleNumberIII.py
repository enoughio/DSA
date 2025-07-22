class Solution:
    def singleNumber(self, arr: List[int]) -> List[int]:
            mymap = {}
            ans = []

            for i in arr :
                if i in mymap :
                    mymap[i]+=1
                else :
                    mymap[i] = 1
            
            for i,n in mymap.items() :
                if n & 1 :  ## == 1 then it is odd
                    ans.append(i)

            return ans  
    



class Solution:
    def singleNumber(self, arr: List[int]) -> List[int]:
        num = 0 

        for i in arr : 
            num = i ^ num
        
        num = (num & num - 1) ^ num

        j = 0
        while ( num & ( 1 << j) ) <= 0 :  
            j+=1
        
        b1 = 0 
        b2 = 0
        for n in arr :
            if n & (1 << j) :
                b1 = b1 ^ n
            else :
                b2 = b2 ^ n

        return ( b1, b2 )
