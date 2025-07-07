class Solution:
    def reverseWords(self, s: str) -> str:

        srt = ''
        i = 0
        n =  len(s)

        while i < n : 
            word =  ''

            while i < n and s[i] != ' ' : 
                word = word + s[i]
                i+= 1
            
            while i < n and s[i] == ' ' :
                i += 1

            if len(srt) > 0 : 
                srt = " " + srt

            srt  = word + srt 
           
            
        return srt

# ==============================================


# this is a O(n) Solution

class Solution:
    def reverseWords(self, s: str) -> str:

        srt = []
        i = 0
        n =  len(s)

        while i < n : 
            word =  ''

            while i < n and s[i] != ' ' : 
                word = word + s[i]
                i+= 1
            
            while i < n and s[i] == ' ' :
                i += 1

            if word : 
                srt.append(word) 
           
        return ' '.join(reversed(srt))

