    ListNode* addBack(ListNode* head, int val){
        ListNode* newHead = new ListNode(val);
        newHead->next = head;
        return newHead;
    }

    ListNode* reverseList(ListNode* head) {

        if(head == NULL || head->next == nullptr){
            return head;
        }
        

        ListNode* temp = head->next;
        head->next = nullptr;

        while(temp != nullptr){
            int val = temp->val;
            head = addBack(head, val);
            ListNode * prev = temp;
            temp = temp->next;
            prev->next = nullptr;
            delete prev;
        }

        return head;
    }