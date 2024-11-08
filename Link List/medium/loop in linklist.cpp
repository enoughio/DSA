class Solution {
public:
    bool hasCycle(ListNode* head) {
        unordered_map<ListNode*, int> mapp;
        ListNode* it = head;
        
        while (it != NULL) {

            if (mapp.find(it) != mapp.end())
                return true;
            else
                mapp[it] = 1;

            it = it->next;
        }
        return false;
    }
};  