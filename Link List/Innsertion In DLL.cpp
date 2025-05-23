#include <bits/stdc++.h>
using namespace std;

class Node
{
public:
    int data;
    Node *next;
    Node *back;

public:
    Node(int data1, Node *next1, Node *back1)
    {
        data = data1;
        next = next1;
        back = back1;
    }

    // public:
    //     Node(int data1, Node *next1)
    //     {
    //         data = data1;
    //         next = next1;
    //         back = nullptr;
    //     }

public:
    Node(int data1, Node *back1)
    {
        data = data1;
        next = nullptr;
        back = back1;
    }

public:
    Node(int data1)
    {
        data = data1;
        next = nullptr;
        back = nullptr;
    }
};

Node *AtoDLL(vector<int> &arr)
{
    Node *head = new Node(arr[0]);
    Node *prev = head;

    for (int i = 1; i < arr.size(); i++)
    {
        Node *temp = new Node(arr[i]);
        prev->next = temp;
        temp->back = prev;
        prev = temp;
    }

    return head;
}

void printList(Node *head)
{
    while (head != nullptr)
    {
        cout << head->data << " -> ";
        head = head->next;
    }
    cout << "nullptr" << endl;
}

Node *DeleteHead(Node *head)
{
    if (head == NULL)
        return head;
    if (head->next == nullptr)
    {
        delete head;
        return NULL;
    }

    Node *prev = head;
    head = head->next;
    head->back = nullptr;
    prev->next = nullptr;
    delete prev;

    return head;
}

Node *DeleteTail(Node *head)
{

    if (head == NULL)
        return NULL;
    if (head->next == nullptr)
    {
        delete head;
        return NULL;
    }

    Node *it = head;

    while (it->next != nullptr)
    {
        it = it->next;
    }

    Node *tail = it->back;
    it->back = nullptr;
    tail->next = nullptr;
    delete it;

    return head;
}

Node *DeleteKInRange(Node *head, int k)
{
    if (head == NULL)
        return NULL;

    Node *it = head;
    int cnt = 0;
    while (it != nullptr)
    {
        cnt++;
        if (k == cnt)
            break;

        it = it->next;
    }

    Node *prev = it->back;
    Node *front = it->next;

    if (prev == nullptr && front == nullptr) // only a single node
    {
        delete it;
        return NULL;
    }
    if (prev == nullptr)
    {
        return DeleteHead(head);
    }
    if (front == nullptr)
    {
        return DeleteTail(head);
    }

    prev->next = front;
    front->back = prev;

    delete it;
    return head;
}

Node *DeleteK(Node *head, int k)
{
    if (head == NULL)
        return NULL;
    if (head->next == nullptr)
    {
        delete head;
        return NULL;
    }
    if (k == 1)
        return DeleteHead(head);

    Node *it = head;
    int cnt = 0;
    while (it != nullptr)
    {
        cnt++;
        if (k == cnt)
        {
            if (it->next == nullptr)
            {
                Node *prev = it->back;
                prev->next = nullptr;
                it->back = nullptr;
                delete it;

                return head;
            }

            Node *prev = it->back;
            prev->next = it->next;

            it->next = nullptr;
            it->back = nullptr;
            delete it;

            return head;
        }

        it = it->next;
    }

    return head;
}

Node *DeleteAtVal(Node *head, int val)
{
    if (head == NULL)
        return NULL;
    if (head->data == val)
        return DeleteHead(head);

    Node *it = head;
    while (it != nullptr)
    {

        if (it->data == val)
        {
            if (it->next == nullptr)
            {
                Node *prev = it->back;
                prev->next = nullptr;
                it->back = nullptr;
                delete it;

                return head;
            }

            Node *prev = it->back;
            prev->next = it->next;

            it->next = nullptr;
            it->back = nullptr;
            delete it;

            return head;
        }

        it = it->next;
    }

    return head;
}

Node *InsertAtStart(Node *head, int data)
{
    if (head == NULL)
    {
        Node *newHead = new Node(data);
        return newHead;
    }
    Node *newHead = new Node(data);

    head->back = newHead;
    newHead->next = head;

    return newHead;
}

Node *InsertAfterTail(Node *head, int data)
{
}
Node *InsertBeforeTail(Node *head, int data)
{
    if (head == NULL)
        return new Node(data);
    if (head->next == nullptr)
    {
        Node *newNode = new Node(data);
        head->next = newNode;
        newNode->back = head;
        return head;
    }

    Node *it = head;
    while (it->next->next != nullptr)
    {
        it = it->next;
    }

    Node *newNode = new Node(data);
    it->next->back = newNode;
    newNode->next = it->next;

    it->next = newNode;
    newNode->back = it;

    return head;
}

Node *InsertBeforKth(Node *head, int data)
{
    
}

int main(void)
{
    vector<int> arr = {1, 2, 3, 55, 4};
    Node *head = AtoDLL(arr);
    // printList(head);
    // head = DeleteHead(head);
    // DeleteTail(head);
    // head = DeleteAtVal(head, 89009);
    // head = DeleteK(head, 2);
    // head = DeleteKInRange(head, 3);
    // head = InsertAtStart(head, 0);
    head = InsertBeforeTail(head, 44);
    printList(head);
}