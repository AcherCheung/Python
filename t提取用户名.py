def suffix(filename):
    #从字符串查找.出现的位置
    pos = filename.find('.')
    print(pos)
    return filename[pos + 1:] if pos > 0 else ''


print(suffix('11111hah.json'))
print(suffix('.txt'))
