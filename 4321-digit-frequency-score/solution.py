class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        a=0
        while n>0:
            a=a+n%10
            n//=10
        return a
