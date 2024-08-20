#include <iostream>
#include <vector>

using namespace std;

// int peak(vector<int>& arr) {
//     int s = 0, n = arr.size() - 1, mid, peak = -1, e = n;

//     while (s <= e) {
//         mid = s + (e - s) / 2;
//         cout<<mid<<endl;

        
//             if (arr[mid] > arr[mid + 1] && arr[mid] > arr[mid - 1])
//             {
//                 cout<<"here"<<endl;
//                 return mid;
//             }
//             else if (arr[mid] > arr[mid + 1] ) {
//                 cout<<"one";
//                 peak = mid;
//                 e = mid - 1;
//             } else if (arr[mid] < arr[mid + 1] ) {
//                 cout<<"two";
//                 peak = mid;
//                 s = mid + 1;
//             }
      
//     }

//     return peak;
// }



int peak(vector<int>& arr) {
        int start = 0;
        int end = arr.size() - 1;
        int mid = 0;
        ios_base::sync_with_stdio(false);
        cin.tie(nullptr);

        while (start <= end) {

            mid = start + (end - start) / 2;

            // if (mid == 0 || mid == arr.size() - 1) {
            //     return mid;
            // }

            // if (arr[mid] < arr[mid + 1]) {
            //     start = mid;
            // }
            // else if (arr[mid - 1] > arr[mid]) {
            //     end = mid;
            // }
            // else {
            //     return mid;
            // }

            if(arr[mid] >= arr[0])
                start = mid + 1;
            else{
                end = mid ;
            }
        }
        
        return start;
    }


int main() {
    vector<int> arr = {2,3,5,0,1};
    int peakIndex = peak(arr);
    cout << "The peak index is: " << peakIndex << endl;
    return 0;
}
