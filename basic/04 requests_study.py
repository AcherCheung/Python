# import requests
#
# resp = requests.get('http://api.tianapi.com/txapi/wxhottopic/index?key=30ae19772e7ac27c7120c6b37a78fc2d')
# if resp.status_code == 200:
#     data_model = resp.json()
#     for news in data_model['newslist']:
#         print(news['index'] + 1)
#         print(news['word'])
#         print('-' * 40)


# import re
# sentence = 'Oh, shit! 你丫是傻叉吗? Fuck you.'
# pureified = re.sub('fuck|shit|dick|[傻煞沙]|[比屄逼叉缺吊屌碉雕]', '*', sentence, flags=re.IGNORECASE)
# print(pureified)

# import csv
# import random
#
# with open('scores.csv', 'w', encoding='utf-8') as file:
#     # writer = csv.writer(file)
#     writer = csv.writer(file, delimiter='|', quoting=csv.QUOTE_ALL)
#     names = ['刘备', '关羽', '张飞', '赵云', '黄忠']
#     writer.writerow(['姓名', '语文', '数学', '英语'])
#     for i in range(5):
#         verbal = random.randint(40, 100)
#         math = random.randint(20, 120)
#         english = random.randint(30, 120)
#         writer.writerow([names[i], verbal, math, english])

# import csv
# with open('scores.csv', 'r', encoding='utf-8') as file:
#     reader = csv.reader(file)
#     for line in reader:
#         print(reader.line_num, end='\t')
#         for char in line:
#             print(char, end='\t')
#         print()

# Excel写数据
'''
import random
import xlwt

student_names = ['关羽', '张飞', '赵云', '马超', '黄忠']
scores = [[random.randint(40, 100) for _ in range(3)] for _ in range(5)]
# 创建工作薄
wb = xlwt.Workbook()
# 创建工作表
sheet = wb.add_sheet('三年二班')
titles = ('姓名', '语文', '数学', '英语')
# 添加表头
for index, title in enumerate(titles):
    # 表内写数据，第0行第index列
    sheet.write(0, index, title)
for row in range(len(scores)):
    sheet.write(row + 1, 0, student_names[row])
    for col in range(len(scores[row])):
        sheet.write(row + 1, col + 1, scores[row][col])
wb.save('考试成绩表.xls')
'''

# import random
# import re
# import time
# import requests
#
# for page in range(1, 11):
#     resp = requests.get(
#         # 请求https://movie.douban.com/top250时，start参数代表了从哪一部电影开始
#         url=f'https://movie.douban.com/top250?start={(page - 1) * 25}',
#         # 如果不设置HTTP请求头中的User-Agent，豆瓣会检测出爬虫程序而阻止我们的请求
#         # User-Agent可以设置为浏览器的标识（可以在浏览器的开发者工具查看HTTP请求头找到）
#         # 由于豆瓣网允许百度爬虫获取它的数据，因此直接将我们的爬虫伪装成百度的爬虫
#         headers={'User-Agent': 'BaiduSpider'}
#     )
#     # 创建正则表达式对象，通过捕获组捕获span标签中的电影标题
#     pattern = re.compile(r'\<span class="title"\>([^&]*?)\<\/span\>')
#     # 通过正则表达式获取class属性为title且标签内容不以&符号开头的span标签
#     results = pattern.findall(resp.text)
#     # 循环变量列表中所有的电影标题
#     for result in results:
#         print(result)
#     # 随机休眠1-3秒，避免获取页面过于频繁
#     time.sleep(random.randint(1, 3))

import random
import time

from lxml import etree
import requests

for page in range(1, 11):
    resp = requests.get(
        url=f'https://movie.douban.com/top250?start={(page - 1) * 25}',
        headers={
            'User-Agent': 'BaiduSpider',
        }
    )
    tree = etree.HTML(resp.text)
    # 通过XPath语法从页面中提取需要的数据
    spans = tree.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]')
    for span in spans:
        print(span.text)
    time.sleep(random.randint(1, 3))