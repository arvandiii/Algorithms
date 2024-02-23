# 27. Remove Element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums) - nums.count(val)
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = 1000
        nums.sort()

        return k