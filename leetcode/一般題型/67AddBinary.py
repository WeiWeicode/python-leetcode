# 67. Add Binary
# Easy
# 6.6K
# 691
# Companies
# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

# 第一種解法說明
# 第一種解決方案使用內置的int()和bin()函數將二進制字符串轉換為整數，
# 相加，再將結果轉換回二進制字符串。切片[2:]用於從二進制字符串中刪除“0b”前綴。

# def addBinary(a, b):
#     return bin(int(a, 2) + int(b, 2))[2:]



class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a, b = b, a
        n = len(a)
        b = '0'*(n-len(b)) + b
        carry = 0
        res = []
        for i in range(n-1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
            if carry % 2 == 1:
                res.append('1')
            else:
                res.append('0')
            carry //= 2
        if carry:
            res.append('1')
        return ''.join(res[::-1])


if __name__ == '__main__':
    a = "11"
    b = "1"
    print(Solution().addBinary(a, b))
    a = "1010"
    b = "1011"
    print(Solution().addBinary(a, b))


# 第二種解決方案也是類似的思路，但它可以處理a和b長度不同的情況，
# 通過在較短的字符串前面添加前導零。它使用for循環遍歷二進制字符串中的數位，
# 從最小有效數位開始，並使用carry變量來跟踪加數位時的任何溢出。
# 它會將結果數位附加到結果字符串中並返回反向順序的最終二進制字符串。