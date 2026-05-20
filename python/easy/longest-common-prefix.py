"""
LEETCODE 14 : https://leetcode.com/problems/longest-common-prefix/
"""


from typing import List

def is_prefix(idx:int, char: str, strs: List[str]):
    for x in strs:
        if len(x)<=idx or x[idx]!=char:
            return False
    return True


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        word1=strs[0]
        for idx, char in enumerate(word1):
            if not(is_prefix(idx, char, strs)):
                return prefix
            prefix = prefix+char
        return prefix