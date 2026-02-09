class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1]*n
        lprod = 1
        rprod = 1
        for i in range(n):
            ans[i] = lprod
            lprod *= nums[i]
        
        for i in range(n-1,-1,-1):
            ans[i] *= rprod
            rprod *= nums[i]
        return ans


        # l = len(nums)
        # answer = []
        # lprod = 1
        # rprod = 1

        # for i in range(l):
        #     lprod *= nums[:i]
        #     rprod *= nums[i:]
        # return [lprod*rprod]
            


        # for i in range(l):
        #     prod *= nums[:i+1:]
        #     answer.append(prod)
        # return answer
             
        