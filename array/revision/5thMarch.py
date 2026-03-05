class Solution:
    def countPairs(self, arr: List[int]) -> int:
        
        n = len(arr)
        powers = []
        cnt = 0

        prev = 1    
        # i need first 21 powers of 2
        for _ in range(22) :        
            powers.append(prev)
            prev = prev * 2 
        

        for i in range(n) : 

            for j in range(i+1,n) : 
                sum = arr[i] + arr[j]
                res = self.find(sum, powers)
                
                if res == True: 
                    cnt+=1

        return cnt

    def find(self, sum, powers) :
        
        i = 0 
        j = 21

        while i <= j : 
            mid = (i+j)//2
            # print(mid, sum)
            if sum == powers[mid] :
                return True
            elif sum < powers[mid] :
                j = mid - 1
            else : 
                i = mid + 1

        return False
    

    # ----------------solved count good meals----------------
    # finally solved


    class Solution:
    def countPairs(self, arr: List[int]) -> int:
        
        n = len(arr)
        powers = []
        cnt = 0
        mp = {}
        mod = (10 ** 9) + 7

        # need first 21 powers of 2
        prev = 1    
        for _ in range(23) :        
            powers.append(prev)
            prev = prev * 2 

        for n in arr : 

            for p in powers :
                if p < n : 
                    continue 
                
                res = p - n 
                cnt += mp.get(res, 0)
                cnt  = cnt % mod
            
            mp[n] = mp.get(n, 0) + 1
        
        return cnt%mod


    