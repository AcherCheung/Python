# 面向对象入门
# class Student:
#     '''学生'''
#     def __init__(self, name, age):
#         '''初始化方法'''
#         self.name = name
#         self.age = age
#
#     def study(self, course):
#         print(f'{self.name}正在学习{course}')
#
#     def play(self):
#         print(f'{self.name}正在玩耍~~~')
#
#     def __repr__(self):
#         return f'{self.name}: {self.age}'
#
#
# stud1 = Student('Frank', 31)
# stud2 = Student('Lucy', 25)
# stud1.study('sience')
# stud2.play()
# stud3 = [stud1, stud2, Student('Acher', 40)]
# print(stud3)


# 数字时钟
'''
import time


class Clock:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.min = minute
        self.sec = second

    def run(self):
        self.sec += 1
        if self.sec == 60:
            self.sec = 0
            self.min += 1
            if self.min == 60:
                self.min = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0

    def show(self):
        return print(f'{self.hour:0>2d}:{self.min:0>2d}:{self.sec:0>2d}')


clock = Clock(23, 59, 59)
while True:
    clock.show()
    time.sleep(1)
    clock.run()
'''

'''
from enum import Enum


class Suits(Enum):
    space, dimond, club, heart = range(4)


for suit in Suits:
    print(f'{suit}:{suit.value}')
'''
'''
# 同时使用可变参数和关键字参数
def calc(*args, **kwargs):
    result = 0
    for arg in args:
        result += arg
    for value in kwargs.values():
        result += value
    return total


print(calc())                  # 0
print(calc(1, 2, 3))           # 6
print(calc(a=1, b=2, c=3))     # 6
print(calc(1, 2, c=3, d=4))    # 10
'''