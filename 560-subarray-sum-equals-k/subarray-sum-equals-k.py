class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr=0
        subcnt=0
        d={0:1}
        for i in nums:
            curr+=i
            req=curr-k
            if req in d:
                subcnt+=d[req]
            d[curr]=d.get(curr,0)+1
        return subcnt
        