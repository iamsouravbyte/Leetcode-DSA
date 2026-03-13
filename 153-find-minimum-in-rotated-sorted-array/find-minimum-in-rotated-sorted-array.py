class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 # left index
        right = len(nums) - 1 # right index

        while left < right:
            mid = (left + right) // 2 # middle index

            if nums[mid] > nums[right]: left = mid + 1
            else: right = mid

        return nums[left]