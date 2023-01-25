# 5. Longest Palindromic Substring
# Medium
# 23.6K
# 1.4K
# Companies
# Given a string s, return the longest 
# palindromic
 
# substring
#  in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"





class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i+1)
            length = max(len1, len2)
            if length > end - start:
                start = i - (length-1)//2
                end = i + length//2
        return s[start:end+1]

    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

if __name__ == '__main__':
    s = "babad"
    print(Solution().longestPalindrome(s))
    s = "abbcbbc"
    print(Solution().longestPalindrome(s))

# 上面這個分數比較高的解法是使用中心擴展的方法來解決最長回文子字串問題
# 這是使用 Manacher 演算法解決最長回文子字串問題的實現。

# longestPalindrome 函數是主要函數，它接收一個字符串作為輸入，並返回最長的回文子字串。首先，函數檢查輸入字符串的長度是否小於 2，如果是，則返回原始字符串，因為長度小於 2 的字符串不能有任何回文子字串。

# 然後，函數將兩個變量start和end初始化為0和0，它們將用於跟踪最長回文子字串的起始和結束索引。

# 然後，函數使用 for 迴圈遍歷輸入字符串。對於字符串中的每個字符，函數調用expandAroundCenter函數，該函數接收輸入字符串，左索引和右索引。expandAroundCenter函數使用 while 迴圈檢查左右索引处的字符是否相同，以及左右索引是否在字符串范围内。如果這些條件都成立，則函數增加右索引並減少左索引。

# 當 while 迴圈退出時，函數返回找到的回文子字串的長度。通過將索引和索引+1作為左索引和右索引，函數能夠檢查偶數長度的回文。

# 然後，longestPalindrome函數比較回文子字串的長度和當前 end 和 start 之間的差距。如果回文子字串的長度大於當前差距，則函數更新 start 和 end 索引。

# 最後，函數返回輸入字符串中 start 和 end 索引之間的子字符串，即最長回文子字串。

# Manacher 演算法比動態規劃算法稍微複雜一些，但它可以在线性時間內解決此問題。



# class Solution:
#     def longestPalindrome(s: str) -> str:
#         n = len(s)
#         start = 0
#         end = 0
#         dp = [[False] * n for _ in range(n)]
    
#         for i in range(n):
#             dp[i][i] = True
        
#         for i in range(n-1, -1, -1):
#             for j in range(i+1, n):
#                 if s[i] == s[j]:
#                     if j-i < 3:
#                         dp[i][j] = True
#                     else:
#                         dp[i][j] = dp[i+1][j-1]
#                 if dp[i][j] and j-i+1 > end-start+1:
#                     start = i
#                     end = j
#         return s[start:end+1]


# if __name__ == '__main__':
#     s = "babad"
#     print(Solution.longestPalindrome(s))
#     s = "cbbd"
#     print(Solution.longestPalindrome(s))



# 這段程式碼使用動態規劃的方法來解決最長回文子字串問題。

# 首先定義一個二維布林陣列 dp[i][j]，表示字符串中從索引 i 到 j 的子字串是否是回文。
# 接著使用兩層迴圈遍歷整個字符串，從長度為 1 的子字串開始，每次遍歷時將子字串長度增加。
# 在遍歷每個子字串時，檢查子字串是否是回文，可以通過比較首尾字符是否相同來判斷，如果相同則檢查其中間的子字串（不包括首尾字符）是否也是回文。如果所有這些條件都成立，則更新最長回文子字串。

# 變數start 和end 用來記錄目前找到的最長回文子字串的起始和結束位置。在內層迴圈中，最內層的 if 敘述句用來更新 start 和 end 變數，如果找到更長的回文子字串。



        


