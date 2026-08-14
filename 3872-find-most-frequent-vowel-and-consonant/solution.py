class Solution:
    def maxFreqSum(self, s: str) -> int:
        cd={}
        vd={}
        for i in s:
            if i in 'aeiou':
                if i in vd:
                    vd[i]+=1
                else:
                    vd[i]=1
            else:
                if i in cd:
                    cd[i]+=1
                else:
                    cd[i]=1
        maxc=0
        for i in cd.values():
            maxc=max(maxc,i)
        maxv=0
        for i in vd.values():
            maxv=max(i,maxv)
        return maxc+maxv
