class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_num = set(nums) # We store it in set
        longest = 0 

        for num in set_num:
            if num - 1 not in set_num:
                length = 1

                while num + length in set_num:
                    length +=1

                longest = max(length, longest)

        return longest
        