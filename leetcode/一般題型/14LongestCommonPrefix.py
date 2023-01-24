# 14. Longest Common Prefix
# Easy
# 12.3K
# 3.7K
# Companies
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ''
        return prefix

if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    print(Solution().longestCommonPrefix(strs))
    strs = ["dog","racecar","car"]
    print(Solution().longestCommonPrefix(strs))

# 這是一種在 Python 中解決最長公共前綴問題的方法。
# 該代碼使用了一個迴圈來遍歷輸入的字符串列表中的所有字符串，
# 並使用 strs[i].find(prefix) 來檢查當前字符串是否以 prefix 作為前綴。
# 如果不是，則將 prefix 的最後一個字符刪除，並再次檢查。
# 這個過程將繼續進行直到找到最長公共前綴或 prefix 為空。
# 如果 prefix 為空，則返回空字符串，否則返回 prefix。