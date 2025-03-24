# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
         
         head2 = None
         it = head

         while it != None :
            tp = ListNode(it.val)
            tp.next = head2
            head2 = tp

            it = it.next
        
         while( head != None ) :
            if(head.val != head2.val):
                return False
            
            head = head.next
            head2 = head2.next
            
         return True