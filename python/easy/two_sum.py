from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nums = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in seen_nums:
                return [seen_nums[complement],i]
            seen_nums[num] = i
        return []
    
sol = Solution()
res = sol.twoSum([2,7,11,15],9)
print(res)