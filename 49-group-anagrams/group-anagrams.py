from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)  # if key doesn't exist, Python creates an empty list
        result = []  # stores final result

        for s in strs:
            sorted_s = tuple(sorted(s))  # sorted string used as key
            anagram_map[sorted_s].append(s)

        for value in anagram_map.values():
            result.append(value)

        return result