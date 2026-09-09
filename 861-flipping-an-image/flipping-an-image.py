class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n=len(image)
        for i in image:
            l,r=0,n-1
            while l<=r:
                if i[l]==i[r]:
                    i[l]^=1
                    if l!=r:
                        i[r]^=1
                l+=1
                r-=1
        return image
