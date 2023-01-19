# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

#  Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]


# Constraints:

# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        return dummy.next


def create_linked_list(lst):
    dummy = ListNode()
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

# 印出答案
list1 = [1, 2, 4]
list2 = [1, 3, 4]
linked_list1 = create_linked_list(list1)
linked_list2 = create_linked_list(list2)

merged_list = Solution().mergeTwoLists(linked_list1, linked_list2)

# 印出答案
while merged_list:
    print(merged_list.val)
    merged_list = merged_list.next
    


# 指針演算法：使用一個dummy node，並使用一個指針指向dummy node，並透過比較兩個區間的起始時間來合併兩個區間，將結果加入結果陣列中。
#
# 1. 比較兩個區間的起始時間，將較小的區間加入結果陣列中。
# 2. 將較小的區間的起始時間往後移一個位置。
# 3. 重複步驟1和2，直到其中一個區間的起始時間超出該區間的範圍。
# 4. 將另一個區間的剩餘區間加入結果陣列中。
# 5. 回傳結果陣列。
#
# 這個演算法的時間複雜度為O(n)，空間複雜度為O(1)。
#
# 驗證
# 1. list1 = [1,2,4], list2 = [1,3,4]  
# 2. list1 = [], list2 = []
# 3. list1 = [], list2 = [0]




# AttributeError: 'list' object has no attribute 'val'
# 這個錯誤是因為list沒有val這個屬性，所以會出現錯誤。


