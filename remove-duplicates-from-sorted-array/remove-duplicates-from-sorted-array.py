class Solution(object):
    def removeDuplicates(self, nums):
        p1 = 0
        p2 = 1
        if len(nums) == 0:
            return 0
        while (p1 < p2 and p2 < len(nums)):
            if nums[p1] == nums[p2]:
                p2 += 1
            else:
                p1 += 1
                nums[p1] = nums[p2]
                p2 += 1
        return p1 + 1
                
        