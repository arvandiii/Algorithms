# 80. Remove Duplicates from Sorted Array II

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        prev_equal = False
        prev = nums[0]
        for i in range(1, len(nums)):
            if prev == nums[i]:
                if prev_equal:
                    nums[i] = 200
                else:
                    k+=1
                    prev_equal = True
            else:
                k += 1
                prev = nums[i]
                prev_equal = False
        nums.sort()
        return k