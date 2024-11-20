






/*      not working
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 
class Solution {
public:

    ListNode * Fmid(ListNode * head){
        ListNode* slow = head;
       ListNode* fast = head;

        while(fast  != nullptr && fast->next != nullptr){
            slow = slow->next;
            fast = fast->next->next;
        }

        return slow;
    }

    ListNode * insert(ListNode * last, int data){
        ListNode * newNode = new ListNode(data);
        last->next = newNode;
        return newNode;
    }

    void divideList(ListNode * low, ListNode * high){
        
        if(mid->next == nullptr || low->next != nullptr) return;    // single node link list 

        mid = Fmid(low);
        low
        divideList(low, mid, high);
        mid = Fmid(mid->next);
        divideList(mid->next, mid, high);
        low = merge(low, mid->next);         // passing starting node of each divided list

    }


    ListNode * merge(ListNode* p1, ListNode* p2){

        // here we create a new list by merging two sorted list 
        ListNode * newHead = nullptr;        

        ListNode * t1 ;                     //iterators for list 1 and 2
        ListNode * t2 ;

        if(p1->val < p2->val){              // setting a head to list
            newHead = p1;
            t1 = p1->next;
            t2 = p2;
        }
        else {
            newHead = p2;
            t2 = p2->next;
            t1 = p1;
        }

        ListNode * last = newHead;         // to track a last inserted node


        while(t1 != p2 && t2 != nullptr){

            if(t1->val < t2->val){
                last = insert(last, t1->val);   // update last
                t1 = t1->next;
            }
            else {
                last = insert(last, t2->val);   // update last
                t2 = t2->next;
            }
        }


        //  for remaining element in 1st sorted list
        while(t1 != p2){
            last = insert(last, t1->val);   // update last
            t1 = t1->next;
        }

         //  for remaining element in 2st sorted list
        while(t2 != nullptr){
            last = insert(last, t2->val);   // update last
            t2 = t2->next;
        }

        return newHead;

    }


    ListNode* sortList(ListNode* head) {
        

        if(head == NULL || head->next == nullptr)   //edge case
            return head;

        ListNode * high = head; 

        int cnt = 0;
        while(high->next != nullptr){   // finding last node of list 
            high = high->next;
            cnt++;
        }
        cout<<cnt;

        divideList(head, high);
        return head;

    }
};

*/