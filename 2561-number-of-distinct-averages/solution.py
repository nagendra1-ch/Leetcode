class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        res=[]
        for i in range(len(nums)//2):
            min1=min(nums)
            max1=max(nums)
            res.append((min1+max1)/2)
            nums.remove(min1)
            nums.remove(max1)
        return len(list(set(res)))
