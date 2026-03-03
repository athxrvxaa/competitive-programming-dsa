class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def invert(s):
            return ''.join('1' if c=='0' else '0' for c in s)
        
        def building_str(n):
            s = '0'
            for _ in range(2,n+1):
                inverted = invert(s)
                reversed_inverted = inverted[::-1]
                s = s + "1" +reversed_inverted
            return s
        value = building_str(n)
        return value[k-1]

        