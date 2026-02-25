class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # bitarr = 
        # for i in range(len(arr)):\
        # sorted_arr=arr.sort()
        # return sorted_arr
        # return (arr, key=(lambda x:bin(x) x.count(1))
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))


        