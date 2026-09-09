class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        k=[]
        l,r=0,0
        n1,n2=len(word1),len(word2)
        while l<n1 and r<n2:
            k.append(word1[l])
            k.append(word2[r])
            l+=1
            r+=1
        k.append(word1[l:])
        k.append(word2[r:])
        return "".join(k)