import os
import time

content = '北 京 欢 迎 你 为 你 开 天 辟 地           '
while True:
    # Windows清除屏幕上的输出
    # os.system('cls')
    # macOS清除屏幕上的输出
    os.system('clear')
    print(content)
    # 休眠0.2秒（200毫秒）
    time.sleep(0.2)
    content = content[1:] + content[0]