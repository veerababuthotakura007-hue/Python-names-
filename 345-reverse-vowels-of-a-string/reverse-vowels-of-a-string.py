class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        l=0
        r=len(s)-1
        v='AEIOUaeiou'
        while l<r:
            if s[l] in v and s[r] not in v:
                r-=1
            elif s[l] not in v and s[r] in v:
                l+=1
            elif s[l] in v and s[r] in v:
                s[l],s[r]=s[r],s[l]
                l+=1
                r-=1
            else:
                l+=1
                r-=1
        return ''.join(s)    