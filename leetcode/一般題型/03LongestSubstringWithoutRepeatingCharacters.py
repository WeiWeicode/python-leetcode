# 3. Longest Substring Without Repeating Characters
# Medium
# 31.6K
# 1.4K
# Companies
# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        right = 0
        chars = set()
        max_len = 0
        while right < n:
            if s[right] not in chars:
                chars.add(s[right])
                max_len = max(max_len, len(chars))
                right += 1
            else:
                chars.remove(s[left])
                left += 1
        return max_len

if __name__ == '__main__':
    s = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s))
    s = "bbbbb"
    print(Solution().lengthOfLongestSubstring(s))
    s = "pwwkew"
    print(Solution().lengthOfLongestSubstring(s))

      
       
# 這個問題可以使用滑動窗口的方法來解決。初始化兩個指針left和right，
# 表示當前子字符串的開始和結尾。遍歷字符串，將每個字符添加到一個集合中。
# 如果當前字符已經在集合中，則從集合中刪除左指針所指的字符，
# 並將左指針移動到右邊。記錄下目前為止看到的最長子字符串的長度，並在最後返回。
# 这种解决方案的时间复杂度为O(n)，空间复杂度为O(min(n, m))，其中n是输入字符串的长度，m是字符集的大小。

# 算法的判断条件就是：

# 当遍历到每一个字符s[right]时，判断s[right]是否在集合chars中出现过。
# 如果没有出现过，将s[right]加入到集合chars中，并将右指针向右移动。
# 如果出现过，则将左指针向右移动，并在集合chars中删除s[left],直到s[right]不再重复为止。
