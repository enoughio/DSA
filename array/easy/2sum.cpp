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



        //python solution
                mapp = {}
        n = len(nums)

        for i in range(n):
            if k - nums[i] in mapp:
                return (i, mapp[k-nums[i]])
            mapp[nums[i]] = i

        return (0,0)