# import pymysql
#
#
# def main():
#     no = int(input('编号： '))
#     name = input('名字：')
#     loc = input('所在地：')
#     con = pymysql.connect(host='10.25.112.88', port=3306,
#                           user='root', password='123456',
#                           database='hrs', charset='utf8')
#     try:
#         # 创建一个可以操作数据库的游标对象
#         with con.cursor() as cursor:
#             result = cursor.execute(
#                 'insert into tb_dept values (%s, %s, %s)',
#                 (no, name, loc)
#             )
#             if result == 1:
#                 print('添加成功!')
#                 con.commit()
#     finally:
#         con.close()
#
#
# if __name__ == '__main__':
#     main()

# redis
