class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        c=0
        max_=0
        for i in gain:
            c+=i
            if c>max_:
                max_=c
        return max_