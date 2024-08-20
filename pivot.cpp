#include <iostream>
#include <vector>

using namespace std;

int findPivot(int arr[], int n)
{

    cout<<"hello form fp"<<endl;

    int s = 0;
    int e = n-1;
    int pivot = 0;

    while (s <= e )
    {   
         int mid = s + ( e - s )/2;
         cout<<mid<<endl;

        if(mid != 0 && mid != n - 1)
        {
            if( arr[mid] < arr[mid + 1] && arr[mid] < arr[mid - 1] )
                return mid;
            
            if(arr[s] <= arr[mid]  )
            {
                pivot = mid;
                s = mid + 1;
            }
            else {
                pivot = mid;
                e = mid - 1;
            }

        } else 
            return mid;
    }
        return pivot;
}



int main() {
    int arr[] = { 3,4,5,1,2};
    int pivot = findPivot(arr, 5);

    cout << "Pivot index: " << pivot << endl;

    return 0;
}