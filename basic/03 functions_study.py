'''
# 装饰器
import random
import time
from functions import wraps


def record_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'download {func.__name__} cost {end_time - start_time:.3f} second!')
        return result

    return wrapper


@record_time
def download(filename):
    print(f'start download {filename}')
    time.sleep(random.randint(1, 9))
    print(f'{filename} download complicated!')


@record_time
def upload(filename):
    print(f'start download {filename}')
    time.sleep(random.randint(2, 4))
    print(f'{filename} download complicated!')


download('python')
upload('python')
# 取消装饰器
download.__wrapped__('gogogo')
upload = upload.__wrapped__
upload('Python从新手到大师.pdf')
'''

'''
import base64
content = '今天是个晴天'
print(base64.b64encode(content.encode()))
content1 = b'5LuK5aSp5piv5Liq5pm05aSp'
print(base64.b64decode(content1).decode())
'''
'''
import sys
# 读取文件
print(sys.getdefaultencoding())
file = open('致橡树.txt', 'r', encoding='utf-8')
print(file.read())
file.close()
'''

'''
import time

file = None
try:
    with open('致橡树.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        print(f'{line}',end='')
except FileNotFoundError:
    print('未找到指定文件')
except UnicodeDecodeError:
    print('读取文件时解码错误')
finally:
    file.close()
'''

'''
import json
my_dict = {
    'name': '张德华',
    'age': 32,
    'friends': ['王大锤', '杜小仙'],
    'cars': [
        {'brand': 'BMW', 'MAX_SPEED': 280},
        {'brand': 'Benz','MAX_SPEED': 260},
        {'brand': 'Audi','MAX_SPEED': 240}
    ]
}
with open('data.json', 'w') as file:
    json.dump(my_dict, file)
print('字典已保存到json文件中！')

# my_dict1 = {}
with open('data.json', 'r') as file1:
    my_dict1 = json.load(file1)
print(type(my_dict1))
 print(my_dict1)
 
'''
