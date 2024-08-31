#include <bits/stdcc++.h>
using namespace std;

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        

        int end = matrix.size();
      
            for(int i = 0; i < end; i++)
            {       
                for(int j = i+1; j < end; j++)
                {
                     swap(matrix[j][i], matrix[i][j]);
                }
            }

            for(int i = 0; i < end; i++)
            {
                reverse(matrix[i].begin(), matrix[i].end());
            }


    }
};




        //    for(int j = 0, k = end - 1; j < k; j++, k--)
        //         {
        //                 swap(matrix[i][j], matrix[i][k]);
        //         }




// brute
    // void rotate(vector<vector<int>>& matrix) {
        

    //     int end = matrix.size();
    //      vector<vector<int>> m(end, vector<int>(end, 0));

      
    //         for(int i = 0; i < end; i++)
    //         {       
    //             for(int j = 0; j < end; j++)
    //             {

    //                 m[j][end-i-1] = matrix[i][j];
                        
    //             }
    //         }

    //         matrix = m;


    // }