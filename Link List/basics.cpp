#include <bits/stdc++.h>
using namespace std;

class Node {
    public:
        int data;
        Node* next;
    
    public:
    Node(int data1, Node* next1){
        data = data1;
        next = next1;
    }

    public:
    Node(int data1){
        data = data1;
        next = nullptr;
    }

    
};

    void printLL(Node * head){
        Node * it = head;

        while(it->next != nullptr)
        {
            cout<<it->data<<" ";
            it = it->next;
        }
    }

    Node * arrtoll(vector<int> &arr){
        Node * head;

        Node * a = new Node(arr[0]);
        head = a;

        Node * mover = head;
        for(int i = 1; i < arr.size(); i++){
            Node * temp = new Node(arr[i]);
            mover->next = temp;
            mover = temp;
        }

       return head;
    }

    bool SearchLL(Node * head, int val){
        Node * it = head;

        while(it->next != nullptr)
        {
           
            if(it->data == val) return true;
            it = it->next;
        }
        return false;
    }


        void insertLL(Node * head, int x){
        Node * it = head;

        while(it->next != nullptr)
        {
            cout<<it->data<<" ";
            it = it->next;
        }

        it->next = new Node(x);
        return head;
    }


int main(){

    // Node * head = new Node(2);
    // Head = a;
    // cout<<Head->data<<"\n";


    // int arr[] = {1,2,3,4,5,6,7};
    vector<int>arr = {23,3,11,4,1,3,6,3,2,2,6,4,0};
    Node*  head = arrtoll(arr);
    head = insertLL(head, 888);
    printLL(head);
    // cout<<SearchLL(head, 6);



}