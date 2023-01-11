# stack舉例
class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

s = Stack()
print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())
# 這是一個簡單的 stack 實作，它有一個 items 屬性，用來儲存 stack 的元素。
# 這個 stack 實作有一個 push 方法，用來將元素加入 stack。
# 這個 stack 實作有一個 pop 方法，用來將元素從 stack 中移除。
# 這個 stack 實作有一個 peek 方法，用來回傳 stack 中最上面的元素。
# 這個 stack 實作有一個 isEmpty 方法，用來判斷 stack 是否為空。
# 這個 stack 實作有一個 size 方法，用來回傳 stack 中元素的數量。
