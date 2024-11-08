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
    ListNode* detectCycle(ListNode* head) {

        if (head == NULL || head->next == NULL)
            return NULL;

        ListNode* slow = head;
        ListNode* fast = head;
        int cnt = 0;

        while (fast != NULL && fast->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;
            cnt++;

            if (fast == slow) {
                slow = head;
                while (fast != NULL && fast != slow) {

                    fast = fast->next;
                    slow = slow->next;
                    cnt++
                }

                return cnt;
            }
        }

        return NULL;
    }
};