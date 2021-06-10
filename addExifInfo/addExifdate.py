# !/usr/bin/env python
# -*- coding: utf-8 -*-  
import os
import time
import exifread
from PIL import Image, ImageDraw, ImageFont, ExifTags

'=================分割线==================='


# 创建文件夹
def mymkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)


# 判断是否是支持的文件类型
SUFFIX_FILTER = ['.jpg', '.png', '.mpg', '.thm', '.bmp', '.jpeg']  # 仅测试了jpeg，jpg


def isTargetedFileType(filename):
    '根据文件扩展名，判断是否是需要处理的文件类型；仅支持x.x格式'
    filename_nopath = os.path.basename(filename)
    f, e = os.path.splitext(filename_nopath)
    if e.lower() in SUFFIX_FILTER:
        return True
    else:
        return False


# 新文件的名字
def get_new_filename(filename):
    f, e = filename.split('.')
    return "%s_watermark.%s" % (f, e)


'=================分割线==================='

'=================begin{得到照片的拍摄时间}==================='


def getPhotoTime(filename):
    '''得到照片的拍照时间（如果获取不到拍照时间，则使用文件的创建时间）
    '''
    try:
        if os.path.isfile(filename):
            fd = open(filename, 'rb')
        else:
            raise "[%s] is not a file!\n" % filename
    except:
        raise "unopen file[%s]\n" % filename

    # 默认用图像文件的创建日期作为拍摄日期（如果有照片的拍摄日期，则修改为拍摄日期
    state = os.stat(filename)
    dateStr = time.strftime("\'%y %m %d", time.localtime(state[-2]))

    data = exifread.process_file(fd)
    if data:  # 取得照片的拍摄日期，改为拍摄日期
        try:
            t = data['EXIF DateTimeOriginal']  # 转换成 yyyy-mm-dd_hh:mm:ss的格式
            print(t)
            dateStr = t.strftime('\'%y %m %d')
            # t = time.strftime('\'%y-%m-%d %h:%m:%s', photoDate)
            dateStr = str(t).replace("-", " ")[:9]  # + str(t)[10:]
        except:
            pass

    return dateStr


'=================end{得到照片的拍摄时间}==================='


def orientate(img):
    '''对于手机、相机等设备拍摄的照片，由于手持方向的不同，拍出来的照片可能是旋转0°、90°、180°和270°。即使在电脑上利用软件将其转正，他们的exif信息中还是会保留方位信息。
        在用PIL读取这些图像时，读取的是原始数据，也就是说，即使电脑屏幕上显示是正常的照片，用PIL读进来后，也可能是旋转的图像，并且图片的size也可能与屏幕上的不一样。
        对于这种情况，可以利用PIL读取exif中的orientation信息，然后根据这个信息将图片转正后，再进行后续操作，具体如下。
    '''
    try:
        orientation = None
        for i in ExifTags.TAGS.keys():
            if ExifTags.TAGS[i] == 'Orientation':  # 肯定会找到orientation，所以不需要对None做处理
                orientation = i
                break
        exif = dict(img._getexif().items())
        if exif[orientation] == 3:
            img = img.rotate(180, expand=True)
        elif exif[orientation] == 6:
            img = img.rotate(270, expand=True)
        elif exif[orientation] == 8:
            img = img.rotate(90, expand=True)
    except:
        pass
    return img


def add_watermark(filename, photoTime):
    '为照片文件添加水印，filename是照片文件名，text是水印时间和位置'
    # 创建输出文件夹
    outdir = 'watermark/'
    mymkdir(outdir)

    # 创建绘画对象
    image = Image.open(filename)
    image = orientate(image)  # 将图片转正
    draw = ImageDraw.Draw(image)
    width, height = image.size  # 宽度，高度
    size = int(0.03 * width)  # 字体大小(可以调整0.04)
    cur_path = os.path.abspath(__file__)
    parent_path = os.path.abspath(os.path.dirname(cur_path) + os.path.sep + ".")
    fontfile_path = parent_path + '\mtc7seg.ttf'
    myfont_date = ImageFont.truetype(fontfile_path, size=size)  # 80, 4032*3024
    # fillcolor= '#000000' # RGB黑色
    fillcolor = '#ff9515'

    #根据横竖屏使用不同的水印位置
    width=image.width
    height=image.height
    # 横屏
    if width > height:
        # 参数一：位置（x轴，y轴）；参数二：填写内容；参数三：字体；参数四：颜色
        d_width, d_height = 0.73 * width, 0.87 * height  # 字体的相对位置（胶卷位置）
        draw.text((d_width, d_height), photoTime, font=myfont_date, fill=fillcolor)  # (-1200, -320)
        new_filename = get_new_filename(filename)
        image.save(outdir + new_filename)
    else:
        # 参数一：位置（x轴，y轴）；参数二：填写内容；参数三：字体；参数四：颜色
        d_width, d_height = 0.74 * width, 0.92 * height  # 字体的相对位置（胶卷位置）
        draw.text((d_width, d_height), photoTime, font=myfont_date, fill=fillcolor)  # (-1200, -320)
        new_filename = get_new_filename(filename)
        image.save(outdir + new_filename)




def scandir(startdir):
    '遍历指定目录，对满足条件的文件进行改名或删除处理'
    os.chdir(startdir)  # 改变当前工作目录
    for obj in os.listdir(os.curdir):
        if os.path.isfile(obj):
            if isTargetedFileType(obj):  # 对满足过滤条件的文件，加时间和地点水印
                photoTime = getPhotoTime(obj)  # 获得照片的拍摄时间,当作水印的内容
                print("%s    %s" % (obj, photoTime ))
                add_watermark(obj, photoTime)  # 加时间


if __name__ == "__main__":
    path = "D:/pics/20210604原始导出"  # 照片位置
    scandir(path)
