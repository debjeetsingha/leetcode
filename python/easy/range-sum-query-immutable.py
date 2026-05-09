"""
Link: https://leetcode.com/problems/range-sum-query-immutable/
"""

# brute force approach

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])


# using prefix sums

class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = []
        cur_sum = 0
        for x in nums:
            cur_sum+=x
            self.prefix.append(cur_sum)
            
    def sumRange(self, left: int, right: int) -> int:
        if left==0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
