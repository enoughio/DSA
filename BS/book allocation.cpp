        bool isvalid(int max, vector<int>& nums, int m ){
        
        int sum = 0;
        for(int i: nums){
            
            if(sum + i <= max){
                sum += i;
            }else{
                sum = i;
                m--;
                if(m == 0) return true;
            }
        }

        return false;
    }


int findPages(vector<int>& arr, int n, int m) {


    // 1. Each student gets at least one book.
    // 2. Each book should be allocated to only one student.
    // 3. Book allocation should be in a contiguous manner.

    if(m > n) return -1;
    
    int ans = -1;
    int sum = 0;
    
    for(int i = 0; i < n; i++)
        sum += arr[i];
    
    int max = *max_element(arr.begin(), arr.end());
    int s = max;
    int e = sum;

    while(s <= e){

        int mid = (e+s)/2;

        if(isvalid(mid, arr, m) == true){
            ans = mid;
            s = mid + 1;
        } else{
            e = mid -1; 
        }
    }

    return s;
}



