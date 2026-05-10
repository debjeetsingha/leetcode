"""
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

update approach later
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        max_len = 0
        str_det = {} # {str: [count, last_seen_idx]}
        l=0
        cur_count = 0
        for r in range(len(s)):
            if s[r] not in str_det:
                str_det[s[r]] = [0,-1]
                
            str_det[s[r]][0] += 1
            str_det[s[r]][1] = r
            cur_count += 1


            while str_det[s[r]][0] > 1:
                str_det[s[l]][0] -= 1
                l = l+1
                cur_count-=1


            max_len = max(max_len, cur_count)
        return max_len





