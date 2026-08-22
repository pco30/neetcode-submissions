class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        length = 0
        ans = set()

        for R in range(len(s)):
            if s[R] not in ans:
                ans.add(s[R])
            else:
                while s[R] in ans:
                    ans.remove(s[L])
                    L += 1

                ans.add(s[R])

            length = max(length, R-L+1)
        
        return length