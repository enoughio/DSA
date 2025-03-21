# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        it = head
        back = None
        ft = None

        if head == None or head.next == None:
            return head

        while it != None:
            ft = it.next
            it.next = back
            back = it
            it = ft

        return back
