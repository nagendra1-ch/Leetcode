class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ans=set(nums[0])
        for num in nums:
            k=set(num)
            ans=ans&k
        return sorted(ans)
