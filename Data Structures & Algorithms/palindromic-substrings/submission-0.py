class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        # length = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[r] == s[l]:
                # if (r-l+1) > length:
                #     length = r-l+1
                l-=1
                r+=1
                count+=1

            l, r = i, i+1
            while l >= 0 and r < len(s) and s[r] == s[l]:
                # if (r-l+1) > length:
                #     length = r-l+1
                l-=1
                r+=1
                count+=1

        return count
        