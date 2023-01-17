def test(a,b):
    return a+b

def test2(a,b):
    return a*b
# print (test(1,2))

# 裝飾器
def decorator(func):
    def wrapper(*args, **kwargs):
        print('before')
        func(*args, **kwargs)
        print('after')
    return wrapper
print (decorator(test2)(1,2))