class Solution {
  public:
    // Function to sort a linked list of 0s, 1s and 2s.
    Node* segregate(Node* head) {

        // Add code here
        
        Node * HZero = new Node(-1);   
        Node * zero =  HZero;
        
        Node * HOne = new Node(-1);   
        Node * one = HOne;   
        
        Node * HTwo = new Node(-1);   
        Node * two = HTwo;   
        
        Node * temp = head;
        
        
        while(temp != NULL){
            
            if(temp->data == 0)
            {
                zero->next = temp; 
                zero = zero->next;
                 temp = temp->next;
                 continue;
            }else if (temp->data == 1)
            {
                one->next = temp; 
                one = one->next;
                temp = temp->next;
                 continue;
            } else {
                two->next = temp; 
                two = two->next;
                temp = temp->next;
                 continue;
            }
            
           
            
        }
        
        
        zero->next = HOne->next;
        one->next = HTwo->next;
        
        return HZero->next;
        
    }
};