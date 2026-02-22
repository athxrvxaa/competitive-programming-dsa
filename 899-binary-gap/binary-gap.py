class Solution:
    def binaryGap(self, n: int) -> int:
        b = bin(n)[2:]
        max_gap = 0
        last = -1
        
        for i in range(len(b)):
            if b[i] == '1':
                if last != -1:
                    max_gap = max(max_gap, i - last)
                last = i
        
        return max_gap
        # arr = [i for i in bin(n)[2:]]
        # l = len(arr)
        # x = 0
        # y = 0
        # for i in range(l):
        #     if arr[i] == 1:
        #         x = 1
        #         continue
        #     y = 1
        # return x+y

            

