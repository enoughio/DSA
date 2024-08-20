#include <iostream>
#include <vector>

using namespace std;


int root(int n)
{
    int r = 0;
    int s = 0;
    int e = n/2;
    int m = (e+s)/2;

    if(n == 0)
        return 0;
    if(n == 1)
        return 1;
    

    while (s<=e)
    {
        
        if(m*m == n)
            return m;
        else if(m*m < n){
            r = m;
            s = m + 1;
        } else e = m -1;

        m = (e+s)/2;
            
    }

    return r;
}



int main() {
    int n =2;
    
    int peakIndex = root(n);
    cout << "The root index is: " << peakIndex << endl;
    return 0;
}

