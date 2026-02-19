class Solution:
    def increasingTriplet(self, nums):
        min1 = float('inf')
        min2 = float('inf')
        for n in nums:
            if n <= min1:
                min1 = n  
            elif n <= min2:
                min2 = n  
            else:
                return True  
        return False  


        # for i in range(len(nums)):
        #     for j in range(len(nums)+1):
        #         for k in range(len(nums)+2):
        #             if i > j > k and nums[i] >nums[j]> nums[k]:
        #                 return True
        # return False
        