# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None : 
            return head

        ev = []
        od = []

        flag  = True

        c = head
        while c != None : 
            if flag == False : 
                ev.append(c.val)
            else : 
                od.append(c.val)

            flag = not flag
            c = c.next

        c = head

        i = 0
        while od and c != None and i < len(od) : 
            c.val = od[i]
            c = c.next
            i +=1
        
        i = 0
        while ev and c != None and i < len(ev) : 
            c.val = ev[i]
            c = c.next
            i += 1
        
        return head
    

    # --------------------------Better Solution--------------------------

    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None : 
            return head


        od = head
        ev = head.next
        es = ev

        while ev != None and ev.next != None : 

            od.next = od.next.next 
            ev.next = ev.next.next 

            od = od.next 
            ev = ev.next

        od.next = es

        return head





