# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
 

# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"

# 題目說明

# 這是一道題目說明，其中給出了一個題目要求：將一個字串按照 Z 形的順序轉換，
# 並根據給定的行數 numRows 進行轉換。給出了三個範例，
# 分別說明了當 numRows 為 3 或 4 時，對於給定的字串 "PAYPALISHIRING" 進行轉換後的結果。並且當 numRows = 1 時就是原本的字符串

# 題目要求我們寫一個函數 convert(string s, int numRows)，
# 其中 s 是要轉換的字串，numRows 是轉換的行數。函數會回傳轉換後的字串。



class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = len(s)
        cycleLen = 2 * numRows - 2
        res = []
        for i in range(numRows):
            for j in range(0, n - i, cycleLen):
                res.append(s[j + i])
                if i != 0 and i != numRows - 1 and j + cycleLen - i < n:
                    res.append(s[j + cycleLen - i])
        return "".join(res)

if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 3
    print(Solution().convert(s, numRows))
    s = "PAYPALISHIRING"
    numRows = 4
    print(Solution().convert(s, numRows))
    s = "A"
    numRows = 1
    print(Solution().convert(s, numRows))



# 題目解析
# 這段程式碼是一個 Python 的類別 (class)，
# 名為 Solution，它有一個函數 convert()。
# 這個函數接收兩個參數：s 是一個字串，numRows 是一個整數。
# 函數會將 s 轉換成 Z 形的字符串，並回傳轉換後的字串。

# 首先，如果 numRows 等於 1，則直接回傳 s。
# 然後定義一個變數 n 為字串 s 的長度，
# 另一個變數 cycleLen 為 2 * numRows - 2。
# 再用一個空的 list res 來儲存轉換後的字串。

# 接著使用一個 for 迴圈從 0 開始遞增到 numRows，
# 在每次迭代中再使用一個 for 迴圈從 0 開始遞增到 n - i，
# 並且每次遞增的增量為 cycleLen。
# 在每次迭代中，將 s[j + i] 加入 res，
# 並且如果 i 不等於 0 且不等於 numRows - 1，
# 且 j + cycleLen - i 小於 n，則將 s[j + cycleLen - i] 加入 res。

# 最後將 res 中的所有元素連接成一個字串，回傳轉換後的字串。