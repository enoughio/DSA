class Solution {
  public:
    Node* constructDLL(vector<int>& arr) {
        
           Node *head = new Node(arr[0]);
    Node *back = head;

    for (int i = 1; i < arr.size(); i++)
    {
        Node *temp = new Node(arr[i]);
        back->next = temp;
        temp->prev = back;
        back = temp;
    }

    return head;
        
    }
};