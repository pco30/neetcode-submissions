class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        L = 0
        ans = ""

        for R in range(len(s2)):
            ans += s2[R]

            if R-L+1 > k:
                ans = ans[1:]
                L += 1
            
            if sorted(ans) == sorted(s1):
                return True

        return False