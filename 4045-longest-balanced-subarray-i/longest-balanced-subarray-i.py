class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            evens = set()
            odds = set()

            for j in range(i, n):
                if nums[j] % 2 == 0:
                    evens.add(nums[j])
                else:
                    odds.add(nums[j])

                if len(evens) == len(odds):
                    ans = max(ans, j - i + 1)

        return ans
# class Solution:
#     def longestBalanced(self, nums: List[int]) -> int:
#         ec = 0
#         oc = 0
#         s = set(nums)
#         for i in s:
#             if i % 2 == 0:
#                 ec +=1
#             else:
#                 oc += 1
#         if ec == oc:
#             return len(nums)
#         else:
#             oc -= 1
#             if ec == oc:
#                 return len(nums) -1



        