class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = [] # result array
        count = Counter(nums) # automatically counts how many times items appear

        sorted_items = sorted(count.items(), key = lambda X : X[1], reverse = True)

        for i in range(k):
            result.append(sorted_items[i][0])

        return result
        