class Solution(object):
    def twoSum(self, nums, target):
       seen = {} # empty dictionary

       for i, num in enumerate(nums):
        diff = target - num
        
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
                
