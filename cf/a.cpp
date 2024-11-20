#include <iostream>
#include <vector>

using namespace std;

int main(){
    int T ;
    cin >> T;
    while(T--){
        int n ;
        cin >> n;
        vector<int> v(n);
        for(auto &x : v){
            cin >> x;
        }
        int ans = 0 ;
        vector<int> used(n , 0);
        for(int i = 0; i < n;i++){
            for(int j = i + 1 ; j < n ; j++){
                if(v[i] == v[j] && !used[j] && !used[i]){
                    used[j] =1 ;
                    used[i] = 1 ;
                    ans++;
                }
            }
        }
        cout << ans << endl;
    }
}