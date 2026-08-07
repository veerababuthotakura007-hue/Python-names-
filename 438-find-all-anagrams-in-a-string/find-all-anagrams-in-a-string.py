class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d1={}
        d2={}
        for i in p:
            d2[i]=d2.get(i,0)+1
        left=0
        ans=[]
        for r in range(len(s)):
            d1[s[r]]=d1.get(s[r],0)+1
            if r>=len(p)-1:
                if d1==d2:
                    ans.append(left)
                d1[s[left]]-=1
                if d1[s[left]]==0:
                    d1.pop(s[left])
                left+=1
        return ans
            