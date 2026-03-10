class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sortedstring = ''.join(sorted(s))
        t_sortedstring = ''.join(sorted(t))

        if s_sortedstring == t_sortedstring: return True
        else: return False