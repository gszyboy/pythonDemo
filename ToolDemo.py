#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-01-09 10:03:40
# @Author  : 如风 (26982310@qq.com)
# @Link    : http://blog.youmaku.top
# @Version : $Id$
import os
from customTools.fetchDocx import fetch
import thulac
from collections import Counter
from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import random

font = os.path.abspath(os.path.join(os.getcwd(),r'font/fzzhjt.TTF'))
fetch = fetch('D:\\DevCode\\一些测试文件','甘肃省档案工作规范化管理办法的通知.docx')
file = fetch.read()


if file['state'] == 1:
    text= file['text']['textString']

thul = thulac.thulac(seg_only=True,user_dict='userDict.txt')
text = thul.cut(text)

a=[]
for v in text:
    while '' in v:
        v.remove('')
    if len(v[0]) >= 2:
        a.append(v[0])
b = Counter(a)
c = dict(b)

height = 1920
width = 1080
img = Image.open('D:\\DevCode\\awesome-python3-webapp\\2.jpg')
img = img.resize((width,height))
img_color = np.array(img)
image_colors = ImageColorGenerator(img_color)
wc = WordCloud(
    background_color="white", #背景颜色
    max_words=200, #显示最大词数
    font_path=font,  #使用字体
    min_font_size=15,
    max_font_size=50, 
    # width=1600,  #图幅宽度
    # height=1500,
    #margin=10,
    scale=3,#值越大越清晰
    prefer_horizontal=1,
    #默认值0.90，浮点数类型。表示在水平如果不合适，就旋转为垂直方向，水平放置的词数占0.9？
    #mask=img_color,
    #random_state=3,
    #color_func=image_colors
    )

d = ' '.join(c)

# wc.generate(d)
wc.generate_from_frequencies(c)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off") #不显示坐标尺寸
plt.show()