class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums)==0:
            return 0
        count=0
        for x in range(len(nums)):
            if nums[x]==val:
                nums[x]=51
            else:
                count+=1
        nums.sort()
        return count
