#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-01-11 11:10:05
# @Author  : 如风 (26982310@qq.com)
# @Link    : http://blog.youmaku.top
# @Version : $Id$

from customTools.doc2docx import Doc2Docx

'''
将doc文件转换为docx文件
'''
path = './Testfile/'#原文件路径
file = 'test.doc'#原文件名称
newpath = './newTestfile/'#新文件路径(非必须的)
newfile = 'newtest'#新文件名称(非必须的)

doc = Doc2Docx(path,file)#传入原文件路径和原文件名
result = doc.tConversion(newPath=newpath,newFile=newfile)#传入新文件路径和新文件名(非必须的)
print(result)#输出dict