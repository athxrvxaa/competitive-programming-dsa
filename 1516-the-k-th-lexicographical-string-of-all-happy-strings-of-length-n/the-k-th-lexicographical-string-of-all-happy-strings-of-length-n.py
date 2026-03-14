class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        res = []
        
        def dfs(curr):
            
            if len(curr) == n:
                res.append(curr)
                return
            
            for ch in "abc":
                if curr and curr[-1] == ch:
                    continue
                
                dfs(curr + ch)
        
        dfs("")
        
        if k > len(res):
            return ""
        
        return res[k-1]
