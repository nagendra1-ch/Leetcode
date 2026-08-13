class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        newBottles=0
        empty=0
        ans=0
        while numBottles>0:
            print(ans)
            ans+=numBottles
            empty+=numBottles
            numBottles=0
            
            numBottles=empty//numExchange

            empty=empty%numExchange

        return ans
