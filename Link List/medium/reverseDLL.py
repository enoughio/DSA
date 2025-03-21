class Solution:
    def reverseDLL(self, head):
        #return head of reverse doubly linked list
        
        if(head == None or head.next == None):
            return head
        
        
        it = head
        ft = None
        
        while(it.next != None):
            ft = it.next
            
            it.next = it.prev
            it.prev = ft
            
            it = ft
            ft = it.next
        
        it.next = it.prev
        it.prev = ft
        
        head = it 
        
        return head
        