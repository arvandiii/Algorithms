# 26. Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == prev:
                nums[i] = 200
            else:
                k+=1
                prev = nums[i]
        nums.sort() 
        return k