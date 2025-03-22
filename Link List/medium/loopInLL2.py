# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        it = head
        dic = {}

        while it != None :

            if it.next in dic :
                return it.next
            
            dic[it] = True
            it = it.next

        return None


node = ListNode(3)
node.next = ListNode(2222222222) 
node.next.next = ListNode(0)
node.next.next.next = ListNode(-4)
node.next.next.next.next = node.next

sol =  Solution()
print(sol.detectCycle(node).val) # 2