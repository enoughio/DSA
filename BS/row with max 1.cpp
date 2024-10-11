class Solution {
  public:
    int rowWithMax1s(vector<vector<int> > &arr) {
        // code here
        int row = arr.size(), col = arr[0].size();
        int ans = -1;
        int mini = col-1;
        
        for(int i = 0; i < row; i++){
            
            int s = 0;
            int e = col-1;
            int f1 = col;
            
            
            while(s <= e){
                int mid = (e+s)/2;
                
                if( arr[i][mid] == 1){
                    e = mid -1;
                    f1 = mid;
                } else {
                    s = mid + 1;
                }
                
            }
            
            
            if( f1 < mini){
                ans = i;
                mini = f1;
            }
            
            
        }
        
        return ans;
        
    }
    
    
};