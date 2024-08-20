#include <bits/stdc++.h>
using namespace std;

vector<int> fib(int n);
vector<int> mul(vector<int>arr, int m);

vector<int> fib(int n)
{ 
    vector<int>v = {1};
  
    if(n == 1 )
        v[0] = 1;
    else
        for(int i = 2; i <= n; i++)
        {
            v = mul(v, i);
        }
        
    return v;
}


// reverse(a.begin(), a.end());
vector<int> mul(vector<int>arr, int m)
{
    int c = 0, n =  arr.size() - 1, x = 0;
    vector<int>v;
    
    for(int i = n; i <= 0; i++)
    {
        x = ( arr[i]*m + c);
        v[n - 1] = x%10;
        c = x/10;
    }

    reverse(v.begin(), v.end());
    
    return v;
}


int main() {
	// your code goes here
    int t;
    cin>>t;
    
    vector<int>v;
    
    while(t--)
        {
            int n; 
            cin>>n;
            
            v = fib(n);
            
            for(int i = 0; i < v.size(); i++)
                cout<<v[i];
            cout<<endl;
        }
    
}



/*
#include <bits/stdc++.h>
using namespace std;

vector<int> fib(int n);
vector<int> mul(vector<int>arr, int m);

vector<int> fib(int n)
{ 
    vector<int>v = {1};
  
    if(n == 1 )
        v[0] = 1;
    else
        for(int i = 2; i <= n; i++)
        {
            v = mul(v, i);
        }
        
        for(int i = 0; i < v.size(); i++)
                cout<<v[i];
        
    return v;
}


// reverse(a.begin(), a.end());
vector<int> mul(vector<int>arr, int m)
{
    int c = 0, n =  arr.size() - 1, x = 0;
    vector<int>v;
    
    for(int i = 0; i <= n; i++)
    {
        x = ( arr[i]*m + c);
        v[n - 1] = x%10;
        c = x/10;
    }
    
        while (carry) {
        res[res_size] = carry % 10;
        carry = carry / 10;
        res_size++;
    }

    
    
    return v;
}


int main() {
	// your code goes here
    int t;
    cin>>t;
    
    vector<int>v;
    
    while(t--)
        {
            int n; 
            cin>>n;
            
            v = fib(n);
            
            
            cout<<endl;
        }
    
}




*/

