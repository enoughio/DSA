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

    // basicly create a fale list at the begining wit the values of node then compare it;
    ListNode* InsetPNode(ListNode * pHead, int data){
        
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
};