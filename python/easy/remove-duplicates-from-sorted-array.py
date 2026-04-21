class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_count = 0
        if len(nums)==1:
            return 1
        for x in range(len(nums)):
            if nums[x]==nums[x-1]:
                nums[x-1]=101
            else:
                unique_count += 1
        nums.sort()

        return unique_count

