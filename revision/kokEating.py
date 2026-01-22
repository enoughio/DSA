from math import ceil

h = 8
piles = [3,6,7,11]


class solution : 

    def solve(self, piles, h) : 

        maxPile = max(piles)
        i = 0
        j = maxPile

        while i <= j :             
            rate = (i+j)//2

            totalHours = self.calculateHour(rate, piles)
            
            if totalHours > h : 
                i = rate + 1
            elif totalHours <= h :
                j = rate -1

        return i

    
    def calculateHour(self, rate, piles): 

        total = 0

        for pile in piles : 
            total += ceil(pile/rate) 

        return total
         
        

        