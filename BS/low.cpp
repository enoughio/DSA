        map<long long, int>preSum;
        
        long long sum = 0;
        int maxLen = 0;
        
        for(int i = 0; i < N; i++)
        {
            sum +=A[i];
            
            if(sum == k)
            {
                maxLen = max(maxLen, i+1);
            }
            
            long long rem = sum - k; 
            
            if(preSum.find(rem) != preSum.end())
            {
                int len = i - preSum[rem];
                maxLen = max(maxLen, len);
            }
            
            preSum[sum] = i;
            if(preSum.find(sum) == preSum.end())
                preSum[sum] = i;
                
        }
            return  maxLen;
            