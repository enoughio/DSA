#include <bits/stdc++.h>
using namespace std;

 string n;
 int m;

bool palandrome(int); 

// reversee array n to 1
int main()
{
    cin>>n;
    m = n.length();
    cout<<palandrome(0);
    return 0;

}

bool palandrome( int i)
{
    if(i >= m/2)
        return true;

    if(n[i] != n[m-i-1])
        return false;
        
    return palandrome(i+1);
}

