class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = ""
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        
        while i >= 0 or j >= 0 or carry:
            print(f"剛開始的carry：{carry}")
            if i >= 0:
                carry += int(a[i])
                i -= 1
                print(f"加過i的carry:{carry}")
            if j >= 0:
                carry += int(b[j])
                j -= 1
                print(f"加過j的carry:{carry}")
            print(f"加完後二進位的carry : + {carry % 2}")
            s = str(carry % 2) + s
            carry //= 2
            print(f"最後除二之後的carry:{carry}")
        print(s)
        return s



solution = Solution()

solution.addBinary("110", "111")