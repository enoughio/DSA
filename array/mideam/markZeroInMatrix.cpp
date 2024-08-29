#include <bits/stdc++.h>
using namespace std;


// brute
class Solution {
public:

    void markRow(int i, vector<vector<int>>& matrix, int row )
    {
        for(int k = 0; k < row; k++ )
            matrix[k][i] = -1;

    }

    void markCol(int j, vector<vector<int>>& matrix, int row )
    {
        for(int i = 0; i < col; i++)
        {
            matrix[j][i] = -1;
        }
    }

    void setZeroes(vector<vector<int>>& matrix) {
        
        int row = matrix.size();
        int col = matrix[0].size();

        for(int i = 0; i < row; i++)
        {
            for(int j = 0; j < col; j++)
            {
                if(matrix[i][j] == 0)
                {
                    markRow(i);
                    markCol(j);
                }
            }
        }
        
        for(int i = 0; i < row; i++)
        {
            for(int j = 0; j < col; j++)
            {
                if(matrix[i][j] == -1)
                {
                   matrix[i][j] = 0;
                }
            }
        }
        

        return;
    }
};


//Better solution
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        
        int row = matrix.size();
        int col = matrix[0].size();
        int Col[col];
        int Row[row];

        for(int i = 0; i < row; i++)
        {
            for(int j = 0; j < col; j++)
            {
                if(matrix[i][j] == 0)
                {
                    Row[i] = 0;
                    Col[j] = 0;
                }
            }
        }
        
        for(int i = 0; i < row; i++)
        {
            for(int j = 0; j < col; j++)
            {
                if(Row[i] == 0 || Col[j] == 0) 
                {
                   matrix[i][j] = 0;
                }
            }
        }
        

        return;
    }
};






           if(matrix[0][0] == 0)
                { 
                      for(int i = 0; i < col; i++)
                      {
                        matrix[0][i] = 0;
                      }
                }

     
    
      
                if(col0 == 0)
                {  
                     for(int i = 0; i < row; i++)
                     {
                       matrix[i][0] = 0;
                     }
                }