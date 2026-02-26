class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        decimal_number = int(s,2)
        count = 0
        while decimal_number != 1:
            if decimal_number % 2 == 0:
                decimal_number = decimal_number / 2
                count += 1
            elif decimal_number % 2 != 0:
                decimal_number = decimal_number + 1
                count += 1
        return count

        