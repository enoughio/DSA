class Solution:
	def findLargest(self, arr):
	    # code here
	    n = len(arr)
        for i in range(n) : 
            for j in range(i+1, n) :
                st1 = f'{arr[i]}{arr[j]}'
                st2 = f'{arr[j]}{arr[i]}'
                
                if int(st1) < int(st2) : 
                    temp = arr[i]
                    arr[i] = arr[j] 
                    arr[j] = temp
        st = ''
        flag = True
        for i in arr : 
            if int(i) != 0 : 
                flag = False
            st += str(i)
                
        return st if flag == False else 0