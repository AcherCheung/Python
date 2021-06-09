# r = float(input('please input a num: '))
# p = 2 * 3.1415 * r
# a = 3.14 * r * r
# print('周长为： %.3f' % p)
# print('面积为：%.3f' % a)

# username = input('please input username: ')
# password = input('please input password: ')
# if username == 'admin' and  password == '123456' :
#     print('login is successful')
# else:
#     print('you have no rights to login')

# total = 0
# for i in range(1, 101):
#     total += i
# print(total)

# 猜数字
# import random
# answer = random.randint(1, 100)
# counter = 0
# while True:
#     counter += 1
#     x = int(input(' input some num:  '))
#     if x > answer:
#         print('samaller')
#     elif x < answer:
#         print('bigger')
#     else:
#         print("bingo!")
#         break
# print('you\'re call : %d' % counter)

# 阶乘--函数的引入
# def fac(num):
#     result = 1
#     for i in range(1, num+1):
#         result *= i
#     return result
#
#
# m = int(input('input m: '))
# n = int(input('input n: '))
# res = fac(m) // fac(n) // fac(m-n)
# print(res)

# # 可变参数
# def add(*args):
#     total = 0
#     for n in args:
#         total += n
#     return total
#
#
# print(add(1, 2, 3))
# print(add(4, 5, 7, 3))

# a = 321
# b = 123
# print(f'{a} * {b} = {a * b}')

# 输出文件名
# def suffix(filename):
#     pos = filename.rfind('.')
#     return print(filename[pos + 1:] if pos > 0 else '')
#
#
# suffix("txt.txt")
# suffix('1.exe')
# suffix('.reload')

# # 列表遍历
# items = ['Python', 'Java', 'Go', 'Kotlin']
# for index in range(len(items)):
#     print(items[index])

# 列表生成
# items = []
# for x in range(1, 10):
#     items.append(x)
#     print(items)

# 元组生成
# tuple = ('apple', 'sumsing', 222)
# for x in tuple:
#     print(x)
# print( 222 in tuple)
# print(tuple[1])
#
# a = ()
# b = (100)
# c = (100,)
# print(type(a))
# print(type(b))
# print(type(c))

# 计算指定的年月日是这一年的第几天
# def is_leap_year(year):
#     # 能被4整除且不能被100整除的为闰年,或者年份除以400为0
#     return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
# def which_days(year, month, day):
#     days_of_month = [
#         [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
#         [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     ]
#     days = days_of_month[is_leap_year(year)]
#     total = 0
#     for x in range(month - 1):
#         total += days[x]
#     return total + day
#
# print(which_days(1988, 12, 31))

"""
幸运的女人(约瑟夫环问题)

Version: 0.1
Author: 骆昊
"""
# persons = [True] * 30
# # counter - 扔到海里的人数
# # index - 访问列表的索引
# # number - 报数的数字
# counter, index, number = 0, 0, 0
# while counter < 15:
#     if persons[index]:
#         number += 1
#         if number == 9:
# #             persons[index] = False
#             counter += 1
#             number = 0
#     index += 1
#     index %= 30
# for person in persons:
#     print('女' if person else '男', end='')

# ===================================

# set1 = set('45')
# set1.add('33')
# print(set1)
#
# list1 = [1,]
# print(list1)
#
# tuple1 = (1, 2)
# print(tuple1)

#  ================字典=============
# person = {'name': 'Mr.Wang', 'age': '55', 'weight': '60', 'office': '双子大厦4401'}
# print('name' in person,'tel' in person)
# if 'age' in person:
#     person['age'] = 31
#     person['tel'] = '17638581306'
#     print(person)
#
# for key in person:
#     print(f'{key}:{person[key]}')

#  嵌套字典
# students = {
#     1001: {'name': '狄仁杰', 'sex': True, 'age': 22, 'place': '山西大同'},
#     1002: {'name': '白元芳', 'sex': True, 'age': 23, 'place': '河北保定'},
#     1003: {'name': '武则天', 'sex': False, 'age': 20, 'place': '四川广元'}
# }
# print(students.items())
# for key, value in students.items():
#     print(key, '--->', value)
#
# sentence = input('请输入一段话: ')
# counter = {}
# for ch in sentence:
#     if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
#         counter[ch] = counter.get(ch, 0) + 1
# for key, value in counter.items():
#     print(f'字母{key}出现了{value}次.')

# 在一个字典中保存了股票的代码和价格，找出股价大于100元的股票并创建一个新的字典。
# stocks = {
#     'AAPL': 191.88,
#     'GOOG': 1186.96,
#     'IBM': 149.24,
#     'ORCL': 48.44,
#     'ACN': 166.89,
#     'FB': 208.09,
#     'SYMC': 21.29
# }
#
# stocks2 = { key: value for key, value in stocks.items() if value > 100}
# print(stocks2)

import os

if not os.path.exists('a'):
    os.mkdir('a')
if not os.path.exists('a/test.txt'):
    f = open('a/test.txt', 'w')
    f.write('helle,world!')
    f.close()

with open('a/test.txt', 'r') as test:
    lines = test.readlines()
    for txt in lines:
        print(txt)