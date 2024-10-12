class Solution {
public:
    bool binaryRow(vector<int>& arr, int start, int end, int target) {

        int mid;
        while (start <= end) {
            int mid = (end + start) / 2;

            if (arr[mid] == target) {
                return true;
            } else if (arr[mid] < target) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }

        return false;
    }


    bool binaryColumn(vector<vector<int>>& matrix, int startRow, int endRow, int Col, int target) {

        while (startRow <= endRow) {

            int mid = (startRow + endRow) / 2;

            if (matrix[mid][Col] == target){
                return true;
            } else if (matrix[mid][Col] < target){
                startRow = mid - 1;
            } else {
                endRow = mid + 1;
            }
        }

        return false;
    }



    bool searchMatrix(vector<vector<int>>& matrix, int target) {

        // the matrix can be any m*n
        // and sorted in L order

        // start from right corner  r = 0 c = col -1  go till bottom left corner
        // and search in a inverted l shape [0][0] ----  [r][c] ----- [row-1][c]
        // if  target can lies b/w ([0][0] --- [r][c])
        // then search in space row wise [0][0] --- [r][c]  if found return true
        // else if  target can lies b/w ( [r][c] -- [row-1][c] )
        // then search in space column wise [r][c] --- [row-1][c]  if found
        // return true
        // still not found then move down toward  bottom left corner
        //   r++ and c-- till r < row and c < col

        int row = matrix.size(), col = matrix[0].size();
        int r = 0, c = col - 1;

        while (r < row && c >= 0) {

            if (matrix[r][0] >= target && matrix[r][c] <= target) {

                if (binaryRow(matrix[r], 0, c, target))
                    return true;

            } else if (matrix[r][c] > target && matrix[row - 1][c] <= target) {

                if (binaryColumn(matrix, r, row - 1, c, target))
                    return true;
            }

            r++;
            c--;
        }

        return false;
    }
};

// brure search every
// better search each row with binart search