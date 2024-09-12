        // assign number to map with index as value and element as key
        // in a whie loop substract each character with sum 
        // find if the reminder exist in map if yes then return else move on

        map<int, int> mapp;
        int n = nums.size();

        for(int i = 0; i < n; i++)
        {  
            int num =  target - nums[i];

            if(  mapp.find(num) != mapp.end()) {
                return {mapp[num], i };
            } 
            mapp[ nums[i] ] = i;
 
            cout<<mapp[ nums[i] ];           
        }
        return {-1, 1};