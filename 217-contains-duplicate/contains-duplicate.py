class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n=len(set(nums))
        return n!=len(nums)