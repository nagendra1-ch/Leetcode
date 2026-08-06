class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        l=0
        for csize in s:
            if csize>=g[l]:
                l+=1
            if l==len(g):
                break
        return l
