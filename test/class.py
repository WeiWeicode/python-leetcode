# class練習

class testclass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printname(self):
        print(self.name)
    def printage(self):
        print(self.age)
    
    def __str__(self):
        return 'name: ' + self.name + ', age: ' + str(self.age)

    def __int__(self):
        return self.age
    


test = testclass('test', 10)
test.printname()
test.printage()

print(test)

print(int(test))

# 類別繼承
class testclass2(testclass):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.name = name
        self.age = age

    def printname(self):
        print(self.name)
    def printage(self):
        print(self.age)


test2 = testclass2('test2', 20)
test2.printname()
test2.printage()

print(test2)

