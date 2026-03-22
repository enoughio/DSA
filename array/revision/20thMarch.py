# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None or head.next is None : 
            return head
        
        a = None
        b= head
        c = head.next

        while b is not None : 

            c = b.next
            b.next = a
            a = b
            b = c

        # b.next = a
        
        return a

# ----------------------loop in a linked list----------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        

        s = head 
        f = head 

        if head is None :
            return False

        while f.next != None and f.next.next != None :

            s = s.next
            f = f.next.next

            if s == f : 
                return True 
        
        return False
    


    # -----------------------find the starting point of the loop in a linked list----------------------

    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        s = head 
        f = head 

        if head is None or head.next is None :
            return None

        while f.next != None and f.next.next != None :

            s = s.next
            f = f.next.next

            if s == f : 
                f = -1
                break

        # findCycle 
        if f != -1 : 
            return None
        
        f = head
        while True : 

            if s == f : 
                return s

            s = s.next
            f = f.next 



        return None



        # -------------- find the length of the loop in a linked ----------

'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        #code here
        
        #  // find a loop
        #  // find starting pont 
        #  // detect the length of the loop
         
         
        s = head
        f = head 
        start = None 
        cnt = 0
        
        
        while f != None and f.next != None : 
            
            s = s.next
            f = f.next.next
            
            # // find starting point
            if s == f :
                start = s.next
                cnt+=1
                while s != start : 
                    cnt +=1
                    start = start.next
                
                
                break
                    
        return cnt
        
        
        
        