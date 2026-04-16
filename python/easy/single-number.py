from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = nums[0] 
        for x in range(1, len(nums)):
            result = result ^ nums[x]
        return result