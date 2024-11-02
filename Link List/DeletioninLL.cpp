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
    Node *head;

    Node *a = new Node(arr[0]);
    head = a;

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

Node *DeleteAny(Node *head, int n)
{
    if (n == 1)
    {
        return DeleteHead(head);
    }
    Node *it = head;
    int cnt = 1;

    while (it != nullptr)
    {

        if (cnt + 1 == n)
        {
            if (it->next != nullptr)
            {

                Node *temp = it->next->next; // store connection
                delete it->next;
                it->next = temp;
            }
            else
            {
                delete it->next;
                it->next = nullptr;
                return head;
            }
        }

        cnt++;
        it = it->next;
    }
}

int main()
{

    vector<int> arr = {3, 4,3,5,2,5,2,52,6,2};
    Node *head = arrtoll(arr);
    // printLL(head);

    // head = DeleteHead(head);
    printLL(head);
    head = DeleteAny(head,3);
    // head = DeleteTail(head);
    printLL(head);
}