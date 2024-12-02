class Solution {
  public:
    
    Node* reverseList(Node* head) {

        if (head == NULL || head->next == nullptr) {
            return head;
        }

        //better
        Node* temp = head;
        Node* prev = nullptr;

        while (temp != nullptr) {
            Node* front = temp->next;
            temp->next = prev;
            // prev->next = nullptr;
            prev = temp;
            temp = front;
        }

        return prev;
    }
  
  
    Node* addOne(Node* head) {
        // Your Code here
        // return head of list after adding one
        
        int carry = 1;
        
        head = reverseList(head);
        Node * temp = head;
        
        while(temp != NULL){
        
            temp->data = temp->data + carry;
            if(temp->data < 10){
                carry = 0;
                break;
            }else{
                temp->data;
                carry = 1;
            }
          
          temp = temp->next;
          
        }
        
        
       head = reverseList(head);
    
        if(carry != 0){
            Node * newHead = new Node(carry);
            newHead->next = head;
            return newHead;
        }
        
        return head;
        
    
    }
};