/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode * reverse(ListNode * newHead){
        ListNode* prev = nullptr;
        ListNode * front;
        
        while(newHead != nullptr){
            front = newHead->next;
            newHead->next = prev;
            prev = newHead;
            newHead = front;
        }

        return prev;
    }


    bool isPalindrome(ListNode* head) {

        if(head == NULL || head->next == nullptr)
            return true;

        ListNode * slow = head;
        ListNode * fast = head;

        while(fast->next != nullptr && fast->next->next != nullptr){
            slow = slow->next;
            fast = fast->next->next;

        }

        // ListNode * MidHead = slow->next;
        ListNode * MidHead = reverse(slow->next);
        ListNode * second = MidHead;
        ListNode * first = head;

        while(second != nullptr){
            if(first->val != second->val)
                return false;

            first = first->next;
            second = second->next;
        }

        // reverse(slow->next);
        return true;
    }
};

/*
    better
        {

        stack<int> st;
        ListNode* it = head;

        while (it != nullptr) {
            int data = it->val;
            st.push(data);
            it = it->next;
        }
        it = head;
        while (it != nullptr) {
            int data = it->val;
            
            if(data != st.top())
                return false;

            st.pop();
            it = it->next;
        }

        return true;

    }



    brute
    // basicly create a fale list at the begining wit the values of node then
   compare it; ListNode* InsetPNode(ListNode * pHead, int data){

        ListNode* newPHead = new ListNode(data);
        newPHead->next = pHead;

        return newPHead;
    }

    bool isPalindrome(ListNode* head) {

        int data;
        ListNode * it = head;
        ListNode * pHead = head;

        while(it != nullptr){
            data = it->val;
            pHead = InsetPNode(pHead, data);

            it = it->next;
        }
        it = head;

        while(it !=  nullptr){

            if(pHead->val != it->val)
                return false;

            pHead = pHead->next;
            it = it->next;

        }

        return true;


    }
*/