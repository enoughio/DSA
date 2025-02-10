
"""
    class Solution {
    public:
        void setZeroes(vector<vector<int>>& matrix) {
                
            int n = matrix.size(); // row
            int m = matrix[0].size();  // col 

            vector<vector<int>> newMet (n, vector<int>(m,-1));

            for(int i = 0; i < n; i++){
                for(int j = 0; j < m; j++){
                    
                    if(matrix[i][j] != 0 ){
                        if(newMet[i][j] != 0){
                            newMet[i][j] = matrix[i][j];
                        }
                    }
                    else if(matrix[i][j] == 0){

                        for(int k = 0; k < m; k++){
                            newMet[i][k] = 0;
                        }
                        for(int k = 0; k < n; k++){
                            newMet[k][j] = 0;
                        }

                    }
                }
            }

            matrix = newMet;
        }
    };
"""