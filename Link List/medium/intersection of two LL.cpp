/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        
        ListNode * temp1 = headA;
        ListNode * temp2 = headB;
        // map<ListNode*, int> mapp; // Use ListNode* (pointers) as keys
        int t1 = 0, t2 = 0;

        while (temp1 != NULL) {
            // mapp[temp1]++; // Increment the count of the node (by its memory address)
            t1++;
            temp1 = temp1->next; // Move to the next node
        }

        while(temp2 != NULL){
            t2++;
            temp2 = temp2->next;
        }

         temp1 = headA;
         temp2 = headB;

        int diff = abs(t1 - t2);   
        if(t1 > t2){
            while(temp1 != NULL && diff != 0){
                diff--;
                temp1 = temp1->next;
            }
        }else if(t1 < t2){
            while(temp2 != NULL && diff != 0){
                diff--;
                temp2 = temp2->next;
            }
        }

         while (temp1 != NULL && temp2  != NULL) {
            // mapp[temp1]++; // Increment the count of the node (by its memory address)
            
            if(temp1 == temp2)
                return temp1;

            temp2 = temp2->next; // Move to the next node
            temp1 = temp1->next; // Move to the next node
        }


     return NULL;
    }
};





/**
 * brute force
 * 
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        
        ListNode * temp1 = headA;
        ListNode * temp2 = headB;
        map<ListNode*, int> mapp; // Use ListNode* (pointers) as keys

        while (temp1 != NULL) {
            mapp[temp1]++; // Increment the count of the node (by its memory address)
            temp1 = temp1->next; // Move to the next node
        }

        while(temp2 != NULL){
            if( mapp[temp2] == 1)
                return temp2;
                
            temp2 = temp2->next;
        }

     return NULL;
    }
};