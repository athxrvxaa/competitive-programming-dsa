class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)

        for step in range(n):
            right = (startIndex + step) % n
            left = (startIndex - step) % n

            if words[right] == target or words[left] == target:
                return step

        return -1

# class Solution:
#     def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:

#         n = len(words)
#         countr = 0
#         countl = 0
#         for i in range(n):
#             indexr = (i+1)%n
#             countr += 1
#             if words[indexr] == target:
#                 return countr
#             indexl = (i-1)%n
#             countl += 1
#             if words[indexl] == target:
#                 return countl

#             if countr > countl:
#                 return words[countl]
#             else:
#                 return word[countr]