class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        n =  len(intervals)
        intervals.sort(key=lambda x: x[0])

        temp = intervals[0]
        i = 1
        ans = set()
        
        while i < n : 
            
            while i < n and temp[1] >= intervals[i][0] :  
                
                if  temp[1] <= intervals[i][1] : 
                    temp = [  temp[0] ,intervals[i][1]  ]  
                else : 
                    temp = [  temp[0] , temp[1]]  

                i+=1
            
            ans.add(tuple(temp))
            if i < n : 
                temp = intervals[i]
            i+=1
        
        ans.add(tuple(temp))
        return list(ans)