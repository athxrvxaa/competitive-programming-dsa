class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(''.join('0' if i == '1' else '1' for i in bin(n)[2:]),2)
        