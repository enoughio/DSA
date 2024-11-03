#include <bits/stdc++.h>
using namespace std;

class Node
{
public:
    int data;
    Node *next;

public:
    Node(int data1, Node *next1)
    {
        data = data1;
        next = next1;
    }

public:
    Node(int data1)
    {
        data = data1;
        next = nullptr;
    }
};

void printLL(Node *head)
{
    Node *it = head;

    while (it != nullptr)
    {
        cout << it->data << " ";
        it = it->next;
    }
    cout << endl;
}

Node *arrtoll(vector<int> &arr)
{
   

    Node *head = new Node(arr[0]);
   
    Node *mover = head;
    for (int i = 1; i < arr.size(); i++)
    {
        Node *temp = new Node(arr[i]);
        mover->next = temp;
        mover = temp;
    }

    return head;
}

int SearchLL(Node *head, int val)
{
    Node *it = head;

    int cnt = 0;
    while (it != nullptr)
    {
        // cout<<it->data<<" ";
        cnt++;
        if (it->data == val)
            return cnt;
        it = it->next;
    }
    return 0;
}

Node *DeleteHead(Node *head)
{
    if (head == nullptr)
        return head;

    Node *temp = head;
    head = head->next;
    delete temp; // Updated from free(temp) to delete temp
    return head;
}

Node *DeleteTail(Node *head)
{
    Node *temp = head;

    if (head == NULL)
    {
        return nullptr;
    }
    else if (temp->next == nullptr)
    {
        delete temp;
        return nullptr;
    }

    while (temp->next->next != nullptr)
    {
        temp = temp->next;
    }

    delete temp->next;
    temp->next = nullptr;
    return head;
}

Node *DeleteKthElam(Node *head, int n)
{
    if (head == NULL)
        return nullptr;

    if (n == 1)
    {
        return DeleteHead(head);
    }

    Node *temp = head;
    Node *prev = nullptr;
    int cnt = 0;

    while (temp != nullptr)
    {
        cnt++;
        if (cnt == n)
        {
            prev->next =  temp->next;

            delete temp;
            break;
        }
        prev = temp;
        temp = temp->next;
    }

    return head;
}

Node * DeleteAtValue(Node *head, int num){
      
    if (head == NULL)
        return nullptr;

    if (head->data == num)
    {
        return DeleteHead(head);
    }

    Node *temp = head;
    Node *prev = nullptr;

    while (temp != nullptr)
    {
        if (temp->data == num)
        {
            prev->next =  temp->next;

            delete temp;
            break;
        }
        prev = temp;
        temp = temp->next;
    }

    return head;
}

int main()
{

        vector<int> arr = {3, 4, 5, 2, 52, 6};
        Node *head = arrtoll(arr);
    // printLL(head);

    // head = DeleteHead(head);
    // printLL(head);
    // head = DeleteKthElam(head, 7);
    // head = DeleteTail(head);
    head = DeleteAtValue(head, 3);
    printLL(head);
}