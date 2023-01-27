# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.

 

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.


# 題目說明
# 1. 題目要求找到最後一個單字的長度
# 2. 單字是由非空白字元組成的最長字串

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = s[::-1]
        j = i.split()
        
        if len(j) == 0:
            return 0
        return len(j[0])

if __name__ == '__main__':
    s = "Hello World"
    print(Solution().lengthOfLastWord(s))
    s = "   fly me   to   the moon  "
    print(Solution().lengthOfLastWord(s))
    s = "luffy is still joyboy"
    print(Solution().lengthOfLastWord(s))


# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         return len(s.strip().split()[-1])
#strip() 方法是在字符串前後刪除空格或其他預定義字符，這在這個例子中是用來去除字符串頭尾的空格。

# split() 方法是將字符串分割為一個字符串列表。預設情況下，它是以空格分割字符串，所以這個例子中，它是將字符串分成一個單詞列表。

# 所以這個程式碼是將輸入字符串先去除前後空格，再將它分割成一個單詞列表，最後取出最後一個單詞的長度並回傳。
