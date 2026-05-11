"""
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        max_len = 0
        str_det = {} 
        l=0
        for r in range(len(s)):
            if s[r] not in str_det:
                str_det[s[r]] = 0

            str_det[s[r]] += 1

            while str_det[s[r]] > 1:
                str_det[s[l]] -= 1
                l = l+1

            max_len = max(max_len, r-l+1)
        return max_len
