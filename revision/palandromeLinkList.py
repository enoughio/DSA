# Definition for singly-linked list.
# class Listhead:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        

        def reverse(head) : 

            if head is None or head.next is None : 
                return head

            prev = None
            current = head 
            next = None

            while current != None : 
                next = current.next
                current.next = prev

                prev = current 
                current = next
            
            return prev



        if head.next is None : 
            return True

        s = head
        f = head

        while f.next != None and f.next.next != None : 
            s = s.next
            f = f.next.next
            
        
        s = reverse(s.next)
        f = head

        while s is not None and f != None : 
            
            if s.val != f.val :
                return False
            
            s = s.next
            f = f.next
        
        return True



