class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        
        int row = matrix.size();
        int col = matrix[0].size();

        int startingRow = 0, endingRow = row;
        int startingCol = 0, endingCol = col - 1;
        int mid = 0;

        //decide which  row to search 
            // compare starting and ending Col element to target to find the targeted row to serach
        // for(int i = 0; i <= endingCol; i++)
        // {
        //     if(matrix[i][startingCol] == target)
        //         return true;
        //     else if(matrix[i][endingCol] == target)
        //         return true;

        //     if(matrix[i][startingCol] < target && matrix[i][endingCol] > target)
        //         startingRow = i;
        // }    
            // cout<<startingRow;
        //search in deccided row
            // if target is found then return 
            //and find startinCol to search
            while(startingCol <= endingCol)
            {
                mid = (startingCol+endingCol)/2;

                if(matrix[startingRow][mid] == target)
                    return true;
                else if(matrix[startingRow][mid] < target)
                    startingCol = mid+1;
                else    
                    endingCol = mid-1;
            }

        //seach finally in startingCol for the elemant
                while(startingRow <= endingRow)
            {
                mid = (startingRow+endingRow)/2;
                
                if(matrix[mid][startingCol] == target)
                    return true;
                else if(matrix[mid][startingCol] < target)
                    startingRow = mid+1;
                else    
                    endingRow = mid-1;
            }

            return false;
    }
};








//////////////////////////

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        
        int row = matrix.size();
        int col = matrix[0].size();

        int startingRow = 0, endingRow = row;
        int startingCol = 0, endingCol = col - 1;
        int mid = 0;

        //decide which  row to search 
            // compare starting and ending Col element to target to find the targeted row to serach
        // for(int i = 0; i <= endingCol; i++)
        // {
        //     if(matrix[i][startingCol] == target)
        //         return true;
        //     else if(matrix[i][endingCol] == target)
        //         return true;

        //     if(matrix[i][startingCol] < target && matrix[i][endingCol] > target)
        //         startingRow = i;
        // }    
            // cout<<startingRow;
        //search in deccided row
            // if target is found then return 
            //and find startinCol to search
            while(startingCol <= endingCol)
            {
                mid = (startingCol+endingCol)/2;

                if(matrix[startingRow][mid] == target)
                    return true;
                else if(matrix[startingRow][mid] < target)
                    startingCol = mid+1;
                else    
                    endingCol = mid-1;
            }

        //seach finally in startingCol for the elemant
                while(startingRow <= endingRow)
            {
                mid = (startingRow+endingRow)/2;
                
                if(matrix[mid][startingCol] == target)
                    return true;
                else if(matrix[mid][startingCol] < target)
                    startingRow = mid+1;
                else    
                    endingRow = mid-1;
            }

            return false;
    }
};