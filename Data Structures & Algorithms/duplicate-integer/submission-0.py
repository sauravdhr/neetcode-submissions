class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Use set to remove duplicates

        Time: O(n)
        Space: O(n)
        """
        unique_nums = set(nums)
        return len(unique_nums) < len(nums)
