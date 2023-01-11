# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:

# Input: s = "()"
# Output: true

# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

# 題目大意
# 給定一個只包含 '(', ')', '{', '}', '[' 和 ']' 的字串，判斷輸入的字串是否有效。
# 有效的字串條件為：
# 1. 所有的開括號必須被相同類型的括號所關閉。
# 2. 所有的開括號必須被正確的順序所關閉。
# 3. 每個關閉括號都必須有相對應的開括號。
#
# 解題思路
# 這題的解題思路是使用 stack 來解決。
# 1. 如果當前的字元是開括號，則將其加入 stack 中。
# 2. 如果當前的字元是關括號，則檢查 stack 是否為空，如果為空，則直接回傳 False。
# 3. 如果當前的字元是關括號，則檢查 stack 中最上面的元素是否為相對應的開括號，如果是，則將 stack 中最上面的元素移除，如果不是，則直接回傳 False。
# 4. 如果當前的字元是關括號，則檢查 stack 是否為空，如果不為空，則直接回傳 False。
# 5. 如果當前的字元是關括號，則直接回傳 True。
# 6. 如果當前的字元是開括號，則將其加入 stack 中。
# 7. 如果當前的字元是關括號，則檢查 stack 是否為空，如果為空，則直接回傳 False。
# 8. 如果當前的字元是關括號，則檢查 stack 中最上面的元素是否為相對應的開括號，如果是，則將 stack 中最上面的元素移除，如果不是，則直接回傳 False。
# 9. 如果當前的字元是關括號，則檢查 stack 是否為空，如果不為空，則直接回傳 False。
# 10. 如果當前的字元是關括號，則直接回傳 True。

class Solution:
    def isValid(self, s: str) -> bool:        
        
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
                # append() 方法用於在列表的尾部添加新的對象。
            elif char == ')':
                if len(stack) == 0:
                    # len() 方法返回對象（字符、列表、元組等）長度或項目個數。
                    return False
                if stack[-1] == '(':
                    # stack[-1] 為 stack 中最上面的元素。
                    stack.pop()
                else:
                    return False
            elif char == ']':
                if len(stack) == 0:
                    return False
                if stack[-1] == '[':
                    stack.pop()
                    # pop() 方法用於移除列表中的一個元素（默認最後一個元素），並且返回該元素的值。
                else:
                    return False
            elif char == '}':
                if len(stack) == 0:
                    return False
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

# Runtime: 32 ms, faster than 62.86% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 14.3 MB, less than 43.86% of Python3 online submissions for Valid Parentheses.

s = Solution()
print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.isValid("([)]"))
print(s.isValid("{[]}"))


# 第一次檢討
# len 的使用
# 語法結構需要再熟悉 Ex:冒號在if eif else for都要有
# 熟悉單字return,False,True

# 第二次檢討
# stack.append(char) 忘了Tab
# if len(chen) == 0: => if len(stack) == 0: 是丟到stack裡面
# if stack(-1) == "(": 是陣列然後裡面是-1
# elif stack(char) == "(": (錯了) => if stack(char) == "(": (對了)
# if len(char) == 0: => if len(stack) == 0: 是丟到stack裡面

# 第三次檢討
# stack.append(stack) 丟錯對象 => stack.append(char)