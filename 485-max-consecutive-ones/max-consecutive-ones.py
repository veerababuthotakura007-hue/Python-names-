class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        mx_count=0
        for i in nums:
            if i==1:
                c+=1
            elif i==0:
                mx_count=max(c,mx_count)
                c=0
        return max(c,mx_count)

            