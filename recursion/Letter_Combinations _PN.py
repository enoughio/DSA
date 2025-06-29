# Letter Combinations of a Phone Number


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        dictionary =  { 

            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' :  'mno',
            '7' :  'pqrs',
            '8' :  'tuv',
            '9' :  'wxyz'
        }

        n = len(digits)
        
        def rec( arr,  i): 

            if  i == n :
                ans.append(arr)
                return 

            for ch in dictionary[digits[i]]  :
                rec(arr + ch, i + 1 )

        if n == 0 :  return []

        ans = []
        rec('',  0)
        
        return ans
    

    