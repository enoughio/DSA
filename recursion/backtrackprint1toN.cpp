#include <bits/stdc++.h>
using namespace std;

void reccursion(int , int); 

// print n to 1
int main()
{
    int n;
    cin>>n;

    reccursion(n,n);
    return 0;
}


void reccursion(int i, int n)
{
    if(i < 1)
        return;

    reccursion(i-1, n);
    cout<<i;

    return;
}
