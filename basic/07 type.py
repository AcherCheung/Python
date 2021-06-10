# 实例方法
def instancetest(self):
    print('this is an instance method!')


# 类方法
@classmethod
def classtest(cls):
    print('this is a class method!')


# 静态方法
@staticmethod
def statictest():
    print('this is a static method!')


# 创建类
test_property = {'name': 'tom', 'instancetest': instancetest, 'classtest': classtest, 'statictest': statictest}
Test = type('Test', (), test_property)

# 创建对象
test = Test()
# 调用方法
print(test.name)
test.instancetest()
test.classtest()
test.statictest()
