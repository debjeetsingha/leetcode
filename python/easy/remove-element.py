class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        for r in nums:
            if r!=val:
                nums[left]=r
                left+=1
        return left
    