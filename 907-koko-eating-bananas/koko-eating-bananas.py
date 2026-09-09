def caneat(piles,hours_have,k):
    hours_need=0
    for pile in piles:
        hours_need+=math.ceil(pile/k)
    return hours_need<=hours_have
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        while low<high:
            mid=(low+high)//2
            if caneat(piles,h,mid):
                high=mid
            else:
                low=mid+1
        return low
            
        