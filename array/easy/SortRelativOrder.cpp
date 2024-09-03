#include <bits/stdc++.h>
using namespace std;

vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        
        sort(arr1.begin(), arr1.end());

        int n = arr1.size();
        int m = arr2.size();

        vector<int>ans;
        unordered_map<int, int>mapp ;

        for(int i = 0; i < n; i++) {
            mapp[arr1[i]]++;
        }


        for(int i = 0; i < m; i++)
        {
            for(int j = 0; j < mapp[arr2[i]]; j++)
            {
                 ans.push_back(arr2[i]);
            }
        }

        for(int i = m; i < n; i++)
            ans.push_back(arr1[i]);

        return ans;
        
    }



    int main() {

        vector<int> ans;
        vector<int>arr1 = {1,2,3,45,3,6,3,8,7,8,1,3,4,2,5,9,24,4,6,4,6,7};
        vector<int> arr2 = {2,3,4,5,6,7,1,9};
        ans = relativeSortArray(arr1, arr2);

        for(int i : ans)
            cout << i << " ";
        cout << endl;

    }