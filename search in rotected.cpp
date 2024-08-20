#include <iostream>
#include <vector>

using namespace std;



int searcharr(vector<int>& arr, int s, int e, int k)
{
    int mid = s + (e - s)/2;

    while( s <= e ){

        if(arr[mid] == k)
            return mid;
        else if ( arr[mid] < k)
            s = mid + 1;
        else 
            e = mid - 1;
        
        mid = s + (e - s)/2;
    }

    return -1;
    
}



int findPivot(vector<int>& arr, int n)
{
    int s = 0;
    int e = n -1;
    int mid;

    while(s<=e)
    {
        mid = s + ( e - s)/2;

        if(arr[mid] <= arr[0])
            s = mid + 1;
        else 
            e = mid;
    }

    return mid;
}


int search(vector<int>& arr, int n, int k)
{
    // Write your code here.
    // Return the position of K in ARR else return -1.
    int pivot =  findPivot(arr, n);
    int res;

    if( k == arr[pivot])
        return pivot;
    else if( k < arr[pivot - 1])
       res = searcharr(arr, 0, pivot - 2, k);
    else 
       res = searcharr(arr, pivot, n-1, k);

       return res;


}




int main() {
    vector<int> arr = {3,5,3,2,0};

    cout << "The peak index is: " << "peakIndex" << endl;

      int pivot =  findPivot(arr, n);

    int res;
    if( k == arr[pivot])
        return pivot;
    else if( k < arr[pivot - 1])
       res = searcharr(arr, 0, pivot - 2, k);
    else 
       res = searcharr(arr, pivot, n-1, k);

       return res;


    return 0;
}
