class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return (
            sorted(s1[::2]) == sorted(s2[::2]) and
            sorted(s1[1::2]) == sorted(s2[1::2])
        )
        # l1 = len(s1)
        # for i in range(s1):
        #     if s1 != s2:
        #         s[i],s[i+2] == s[i+2] , s[i]
        #         if s1 == s2:
        #             return True
        #     return False

        # return(sorted(s1)==sorted(s2))
        