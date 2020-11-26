class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            for items in nums:
                if nums[i] + items == target and i != nums.index(items):
                    res.append(i)
                    res.append(nums.index(items))
                    return res
        
