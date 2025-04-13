#include <iostream>
#include <vector>   
using namespace std;


class Solution {
    public:
      
      void rev(vector<int> &v, int i, int j){
          if(i >= j){
              return;
          }
          
          swap(v[i], v[j]);
          i++;
          j--;
          rev(v,i,j);
          
      }
    
      void reverseArray(vector<int> &arr) {
          rev(arr, 0, arr.size()-1);
      }
  };
  

  void runner(Solution sol) {
    vector<int> arr = {1, 2, 3, 4, 5};
    sol.reverseArray(arr);
    for (int i : arr) {
        cout << i << " ";
    }
    cout<< "reversed array" << endl;
    cout << endl;
  }

int main() {
    Solution sol;
    runner(sol);
    return 0;
}