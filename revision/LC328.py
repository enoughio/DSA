class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        
        i, j = 0, 0
        for command in commands : 
            if command[0] == 'D' : 
                i += 1
            elif command[0] == 'U' : 
                i -=1
            elif command[0] == 'R' :
                j += 1
            elif command[0] == 'L' : 
                j -= 1


        return (i * n) + j

   

