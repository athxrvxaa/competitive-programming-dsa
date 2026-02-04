class Solution:
    def compress(self, chars: List[str]) -> int:
        i = write = 0

        while i < len(chars):
            j = i
            while j < len(chars) and chars[j] == chars[i]:
                j += 1

            chars[write] = chars[i]
            write += 1

            if j - i > 1:
                for c in str(j - i):
                    chars[write] = c
                    write += 1

            i = j

        return write
        # freq = {}
        # outp = []
        # for ch in chars:
        #     if ch in freq:
        #         freq[ch] += 1
        #     else:
        #         freq[ch] = 1

        # for k,v in freq.items():
        #     outp.append(k)
        #     outp.append(str(v))
        # return len(outp) 

        # length = len(chars)
        # cnt = 0
        # stack = [] 
        # for ch in range(length - 1):
        #     if chars[ch] == chars[ch+1]:
        #         cnt +=1
        #         stack.append(chars[ch])
        #         stack.append(cnt)
        #     else:
        #         pass  
        #     # cnt = 0
        # return stack                             
        