class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = Counter(s)
        print(count)
        count_t = Counter(t)
        return count_s == count_t