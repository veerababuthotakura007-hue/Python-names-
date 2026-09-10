def canship(weights,days_have,capacity):
    days_needed=1
    cweightsum=0
    for i in weights:
        if cweightsum+i<=capacity:
            cweightsum+=i
        else:
            days_needed+=1
            cweightsum=i
    return days_needed<=days_have
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        while low<high:
            mid=(low+high)//2
            if canship(weights,days,mid):
                high=mid
            else:
                low=mid+1
        return low
                    