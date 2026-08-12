class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s=0
        op=[]
        for i in nums:
            s+=i
            op.append(s)
        return op
       