class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sol=[]
        n=len(nums)
        def backtrack(i):
            if i==n:
                s=sorted(sol)
                if s not in res:
                    res.append(s)
                return 
            backtrack(i+1)
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
        backtrack(0)
        return res
