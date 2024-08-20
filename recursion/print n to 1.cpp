#include <bits/stdc++.h>
using namespace std;

void reccursion(int ); 

// print n to 1

int main()
{
    int n;
    cin>>n;

    reccursion(n);

    return 0;
}



void reccursion(int n)
{
    if(n < 1)
        return;

    cout<<n;
    reccursion(n-1);
}