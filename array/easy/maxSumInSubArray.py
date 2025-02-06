






















    # not working

    # int pairWithMaxSum(vector<int> &arr) {
    #     // Your code goes here
        
    #     int smallest = arr[0];
    #     int secSmallest = -1;
    #     int maxi = 0;
    #     int n = arr.size();
        
    #     for( int i = 1; i < n; i++){
    #         int sum = 0;
    #         for(int j = i+1; j < n; j++){
                
    #             if(arr[j] < smallest){
    #                 secSmallest = smallest;
    #                 smallest = arr[j];
    #             }
    #             else if( secSmallest > arr[j]){
    #                 secSmallest = arr[j];
    #             }
    #             sum = smallest + secSmallest;
    #                 maxi = max(maxi, sum);
                
    #         }
    #     }
        
    #     return maxi;
    # }