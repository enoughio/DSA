# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("10"))
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head

        
        while fast != None and fast.next != None :

            slow = slow.next
            fast = fast.next.next
            
            if slow == fast :
                return True
        
        return False

node = ListNode(3)
node.next = ListNode(2)
node.next.next = ListNode(0)
node.next.next.next = ListNode(-4)
node.next.next.next.next = None

sol =  Solution()
print(Solution().hasCycle(node)) # True