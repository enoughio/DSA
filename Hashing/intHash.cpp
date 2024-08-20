#include <bits/stdc++.h>
using namespace std;

int fact(int); 

// print n to 1
int main()
{
    int n;
    cin>>n;
    int arr[n];

    for(int i = 0; i < n; i++)
        cin>>arr[i];
    
    int hash[100] = {0};  // precompute

        for (int i = 0; i < n; i++)
        {
            hash[arr[i]] += 1;
        }

    int q;  // querry
    cin>>q;
    while(q--)
    {
        int num;
        cin>>num;
        cout<<hash[num];
        // fetch
    }

}

