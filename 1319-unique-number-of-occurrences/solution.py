class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter=Counter(arr)
        k=counter.values()
        return len(k)==len(set(k))
