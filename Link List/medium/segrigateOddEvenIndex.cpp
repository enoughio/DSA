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
    ListNode* deleteNode(ListNode* tfd){
        
        ListNode* td = tfd->next;
        tfd->next = td->next;
        tfd = td->next;
        td->next = nullptr;
        delete td;
        return tfd;
    }


    ListNode* insert(ListNode * temp, int data){
        ListNode * front = temp->next;
        ListNode * newNode = new ListNode(data);
        temp->next = newNode;
        newNode->next = front;
        return newNode; 
    }

    ListNode* oddEvenList(ListNode* head) {

        if(head == nullptr || head->next == nullptr)
            return head;
        
        ListNode * temp = head;
        ListNode * tfd = head->next;

        while(tfd != nullptr && tfd->next != nullptr){
            int data = tfd->next->val;
            tfd = deleteNode(tfd);
            temp = insert(temp, data);
        }
        
        return head;
    }
};