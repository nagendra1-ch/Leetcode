class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g=defaultdict(list)
        courses=prerequisites
        for a,b in courses:
            g[a].append(b)
        states=[0]*(numCourses)
        l=[]
        def dfs(node):
            state=states[node]
            if state==2:
                return True
            if state==1:
                return False
            states[node]=1
            for nei in g[node]:
                if not dfs(nei):
                    return False
            states[node]=2
            l.append(node)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return l
