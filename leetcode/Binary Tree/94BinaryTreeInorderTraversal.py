# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Input: root = [1,null,2,3]
# Output: [1,3,2]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
 

# Follow up: Recursive solution is trivial, could you do it iteratively?

# 這題是要求你用 inorder traversal 的方式來遍歷一個 binary tree。
# 這題的解法有兩種，一種是 recursive，一種是 iterative。
# recursive 的解法很簡單，就是用遞迴的方式來遍歷 binary tree。
# iterative 的解法則是用 stack 來模擬遞迴的過程。
# 這題的 iterative 解法是用 stack 來模擬遞迴的過程，我們先將 root 放入 stack 中，然後進入 while 迴圈。
# 在 while 迴圈中，我們先將 stack 中的元素全部放入 left 中，直到 left 為 None。
# 當 left 為 None 時，我們將 stack 中的最上面的元素 pop 出來，並將它的值加入 result 中。
# 然後將 left 指向 pop 出來的元素的 right，並繼續將 left 放入 stack 中，直到 left 為 None。
# 重複上述步驟，直到 stack 為空，並且 left 為 None。
# 最後回傳 result 即可。

# 這題的 recursive 解法很簡單，就是用遞迴的方式來遍歷 binary tree。
# 首先我們定義一個 helper 函式，用來遍歷 binary tree。
# 在 helper 函式中，我們先判斷 root 是否為 None，如果是的話，我們直接回傳。
# 然後我們先遍歷 root 的 left，再將 root 的值加入 result 中，最後遍歷 root 的 right。
# 最後我們回傳 result 即可。

from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        left = root
        while stack or left:
            while left:
                stack.append(left)
                left = left.left
            node = stack.pop()
            result.append(node.val)
            left = node.right
        return result


# 測試

TreeNode1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(Solution().inorderTraversal(TreeNode1))


