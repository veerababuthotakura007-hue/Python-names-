class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #sliding window logic
        mx_avg=-10000000
        left=0
        currentsum=0
        for right in range(len(nums)):
            currentsum+=nums[right]
            if right>=k-1:
                avg=currentsum/k
                mx_avg=max(avg,mx_avg)
                # Subtracting the value on the left
                currentsum-=nums[left]
                left+=1
        return mx_avg