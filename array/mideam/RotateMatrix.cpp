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



    // void rotate(vector<vector<int>>& matrix) {
        
    //     int n = matrix.size();  // row
    //     int m = matrix[0].size();  // col
    //     vector<vector<int>>odd(n, vector<int>(m));

    //     for( int i = 0; i < n; i++){
    //         for(int j = 0; j < m; j++){
    //             odd[j][m-i-1] = matrix[i][j];
    //         }
    //     }

    //     matrix = odd;
    // }



    // in python

    class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)

        for  i in range(n) :
            for j in range( i,n):
                matrix[j][i], matrix[i][j] =  matrix[i][j], matrix[j][i] 
            matrix[i].reverse()


 