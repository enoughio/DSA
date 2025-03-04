//Capacity To Ship Packages Within D Days

class Solution {
public:
    int calDay(vector<int>& weights, int cap, int n){

            int day = 1;
            long long sum = 0;
            int j = 0;
            
            for(int j = 0; j < n; j++){ 

                if(sum + weights[j] <= cap){
                    sum += weights[j];
                } else {
                    sum = weights[j];
                    day++;
                }
            }
        return day;
    }

    int shipWithinDays(vector<int>& weights, int days) {

        int n  = weights.size();
        int max = *max_element(weights.begin(), weights.end());
        // cout<<max;
        int arrSum = 0;
        for(int i : weights){
            arrSum+= i;
        }


        for(int cap  =  max; cap <= arrSum; cap++){  // for capacity search space

            int day = calDay(weights, cap, n);            
            if(day <= days){
                return cap;
            }

        }

        return max;
    }};
        
        // at once kitna
//         // (sum/cap <= 1)
//         int n = weights.size();
//         long long arrSum = 0;
//         for(int i : weights)
//         {
//             arrSum += i;
//         }

//     int cap = 1;
//     while(cap  <= arrSum){

//        int i = 0;
//        int j = i;
//         int sum = 0;
//         int day = 0;

//        while(j < n){

//                 if(sum/cap <= 1){
//                     j++;
//                     sum += weights[j];
//                 } else {
//                     day++;
//                     i++;
//                     j = i;
//                     sum = weights[i];
//                 }

//                 if(day > days){
//                     cap++;
//                     break;
//                 }

//                 if(i == j && sum/cap > 1){
//                     cap++;
//                     break;
//                 }
//             }

//         if(day == days)
//             return cap;
//     }

//     return -1;

//     }
// };



class Solution:

    def check(self, weights: List[int], cap: int ) -> int:
        dayTaken = 1
        n = len(weights)
        i = 0
        summ = 0

        for w in weights:
            if summ+w>cap:
                dayTaken+=1
                summ=0 
            summ+=w

        return dayTaken



    def shipWithinDays(self, weights: List[int], days: int) -> int:
        end = sum(weights)
        st = max(weights)
        ans = end

        if(days == 1):
            return end

        while(st <= end ):
            mid = floor((end + st)/2)
            dayTaken = self.check(weights, mid)
            
            if( dayTaken <= days):
                end = mid-1
                ans = mid
            else : 
                st =mid + 1

        return ans
        