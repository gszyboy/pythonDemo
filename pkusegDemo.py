#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-01-12 14:50:23
# @Author  : 如风 (26982310@qq.com)
# @Link    : http://blog.youmaku.top
# @Version : $Id$

import os
import pkuseg
import customTools.fetchdocx as fdocx
from wordcloud import WordCloud
import matplotlib.pyplot as plt

path = './Testfile/'
file = '分词测试文本.docx'
doc = fdocx.fetchDocx(path,file)
docstr = doc.read()['text']
docstr = docstr['textString']

seg = pkuseg.pkuseg()
text = seg.cut(docstr)

text = ' '.join(text)
font = os.path.abspath(os.path.join(os.getcwd(),r'font/fzzhjt.TTF'))
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
wc.generate(text)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off") #不显示坐标尺寸
plt.show()