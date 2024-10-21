class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
    
        int n = arr1.size();  
        int T = arr2.size();
        //  sort(arr1.begin(), arr1.end());

        int i = 0;   // set intital pointer for arr1

        for (int t = 0; t < T; t++) {   // treversing each element of arr2

            int j = i;                  // initlizing search from last found element in arr1
            while (j < n) {              // searching element in arr1
                if (arr1[j] == arr2[t]) {       // swaping the elem with its right position
                    swap(arr1[j], arr1[i]);       // (buble sort)
                    i++;                           // moving last found poinnter
                }
                j++;                
            }
        }

        sort(arr1.begin()+i, arr1.end());           // sorting remaining element

        return arr1;
    }
};