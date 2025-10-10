
# brute force

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        n = len(fruits)
        mx = 0


        for i in range(n) : 
            
            bt  = {}
            for j in range(i, n) :     
                
                if len(bt) < 2 :
                    if fruits[j] not in bt  :
                        bt[fruits[j]] = 1
                    elif fruits[j] in bt : 
                        bt[fruits[j]] += 1 
                elif len(bt) == 2 :
                    if fruits[j] in bt : 
                        bt[fruits[j]] += 1
                    else : 
                        break
            
            sum = 0
            for key  in bt : 
                sum += bt[key]

            mx = max(mx, sum )
        
        return mx




# --------------Better-----------------


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        n = len(fruits)
        mx = 0


        for i in range(n) : 
            
            st =  set()
            for j in range(i, n) :     
                
                st.add(fruits[j])
                if len(st) > 2 :
                   break

            mx = max(mx, j-i+1)
        
        return mx



# ------optimal-----------------



class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        n = len(fruits)
        mx = 0
        mp = { }

        l = 0
        r = 0

        while r < n:

            if fruits[r] in mp :
                mp[fruits[r]] += 1
            else : 
                mp[fruits[r]] = 1 

            while( len(mp) > 2) : 

                if mp[fruits[l]] == 1  :
                    mp.pop(fruits[l])
                else :
                    mp[fruits[l]] -= 1
                l +=  1  
            
            sum = 0
            for i in mp : 
                sum += mp[i]

            mx = max(mx, sum)
            r += 1


        return mx
