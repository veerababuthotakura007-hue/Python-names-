class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=[i.lower() for i in s if i.isalnum()]
        k=''.join(n)
        l=0
        r=len(k)-1
        while l<r:
            if k[l]==k[r]:
                l+=1
                r-=1
            else:
                return False
        return True
