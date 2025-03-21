
class Solution:
    def beautySum(self, s: str) -> int:
        bsum = 0
        n = len(s)

        for i in range(n):
            cnt = defaultdict(int)  # Only store seen characters
            maxi = 0

            for j in range(i, n):
                cnt[s[j]] += 1  # Fixing wrong index (was s[i], should be s[j])
                maxi = max(maxi, cnt[s[j]])

                # Reset mini before checking the actual minimum
                mini = float('inf')
                for val in cnt.values():
                    mini = min(mini, val)

                bsum += (maxi - mini)

        return bsum









# this is wrong solution
class Solution:
    def beautySum(self, s: str) -> int:
   
        n = len(s)
        bsum = 0

        for i in range(n):
            cnt = [0] * 27  # Initialize frequency counter
            max_elem = s[i]
            sec_max_elem = s[i]

            for j in range(i,n):
                cnt[ord(s[j]) - ord('a')] += 1

                if cnt[ord(s[j]) - ord('a')] > cnt[ord(max_elem) - ord('a')]:
                    max_elem = s[j]
                elif sec_max_elem == max_elem and s[j] != sec_max_elem:
                    sec_max_elem = s[j]
                elif s[j] != max_elem and cnt[ord(s[j]) - ord('a')] > cnt[ord(sec_max_elem) - ord('a')]:
                    sec_max_elem = s[j]

                bsum = cnt[ord(max_elem) - ord('a')] - cnt[ord(sec_max_elem) - ord('a')]

            
            print(cnt)

        return bsum

