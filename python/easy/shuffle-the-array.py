class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l = 0
        r = n
        new_arr = []
        for x in range(n):
            new_arr.append(nums[l])
            l+=1
            new_arr.append(nums[r])
            r+=1
        return new_arr