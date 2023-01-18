class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        x = str(x)
        return x == x[::-1]
        # x[::-] 的意思是從 x 的最後一個字元開始，每次往前取一個字元，直到取完為止。

# x[::-1] 是 Python 中的切片符號，用於返回字符串或列表的反轉。切片符號的格式是 start:stop:step，其中 start 和 stop 是您想要在切片中包含的第一個和最後一個元素的索引，而 step 是每次迭代時要前進的元素數。默認情況下，start 和 stop 設置為列表 / 字符串的開始和結尾，分別為1。所以當你使用 x[::-1] 時，它會從最後一個元素開始，停在第一個元素並向後移動一個元素，返回 x 的反轉。

# x == x[::-1] 檢查 x 是否等於其反轉。如果等於，則為回文，否則不是。

print(Solution().isPalindrome(121)) # True
print(Solution().isPalindrome(-121)) # False
print(Solution().isPalindrome(10)) # False
print(Solution().isPalindrome(111)) # False