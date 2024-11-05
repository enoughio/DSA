#include <bits/stdc++.h>
using namespace std;

class Node
{
public:
    int data;
    Node *next;

public:
    Node(int data1)
    {
        data = data1;
        next = nullptr;
    }

public:
    Node(int data1, Node *next1)
    {
        data = data1;
        next = next1;
    }
};


void printList(Node* head) {
    while (head != nullptr) {
        cout << head->data << " -> ";
        head = head->next;
    }
    cout << "nullptr" << endl;
}

Node *atol(vector<int> &arr)
{

    Node *head = new Node(arr[0]);
    Node *prev = head;

    for (int i = 1; i < arr.size(); i++)
    {
        Node *temp = new Node(arr[i]);
        prev->next = temp;
        prev = temp;
    }

    return head;
}

Node *InsertHead(Node *head, int data)
{

    head = new Node(data, head);
    return head;
}

Node * InsertTail(Node * head, int data){

    if(head == NULL)
        return new Node(data);

    Node * temp = head;
    while( temp->next != nullptr ){
        temp = temp->next;
    }

    temp->next = new Node(data);
    return head;
}



Node *InsertAtKth(Node *head, int data ,int k)
{
    if(head == NULL)
        return new Node(data);
    if(k == 1)
        return InsertHead(head, data);
    
    Node * temp = head;
    Node * prev = nullptr;
    int cnt = 0;

    while(temp != nullptr){

        cnt++;
        if(cnt == k){
            prev->next = new Node(data);
            prev->next->next = temp;
            break;
        }

        prev = temp;
        temp = temp->next;
    }

    return head;
}


Node *fInsertAtelem(Node *head, int data ,int elem)
{
    if(head == NULL)
        return new Node(data);
    if(head->data == elem)
        return InsertHead(head, data);
    
    Node * temp = head;
    Node * prev = nullptr;


    while(temp != nullptr){


        if(temp->data == elem){
            prev->next = new Node(data);
            prev->next->next = temp;
            break;
        }

        prev = temp;
        temp = temp->next;
    }

    return head;
}

Node *InsertOnelem(Node *head, int data ,int elem)
{
    if(head == NULL)
        return new Node(data);
    if(head->data == elem)
        return InsertHead(head, data);
    
    Node * temp = head;
    Node * prev = nullptr;


    while(temp != nullptr){


        if(temp->data == elem){
            Node * remainder = temp->next;
            delete temp;
            temp = new Node(data);
            prev->next = temp;
            temp->next = remainder;
            break;
        }

        prev = temp;
        temp = temp->next;
    }

    return head;
}



int main(void)
{
    vector<int> arr = {1,2,3,4,5,6,7,8};
    Node *head = atol(arr);

    head = InsertHead(head, 0);
    // head = InsertHead(head, -1);
    // head = InsertHead(head, -2);
    // head = InsertTail(head, 9);
    // head = InsertTail(head, 10);
    // head = InsertAtKth(head, 66, 3);
    // head = InsertAtelem(head, 77, 3);
    head = InsertOnelem(head, 77, 1);
    
    
    printList(head);
}
