class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        c=1
        mx_count=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                c+=1
            else:
                mx_count=max(mx_count,c)
                c=1
        return max(mx_count,c)
