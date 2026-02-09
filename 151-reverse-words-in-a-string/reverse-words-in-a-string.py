class Solution:
    def reverseWords(self, s: str) -> str:

        # rs = s[::-1]
        
        # for ch in rs:
        #     if ch != ' ':
        # l = len(s)
        # for ch in range(l-1,-1,-1):
        #     # print(s[ch])
        #     if ch == " ":
        arr = s.split()
        return " ".join(arr[::-1])

            


        