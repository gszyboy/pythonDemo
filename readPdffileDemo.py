#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-01-11 17:47:27
# @Author  : 如风 (26982310@qq.com)
# @Link    : http://blog.youmaku.top
# @Version : $Id$

import os
from customTools.fetchpdf import fetchPdf

pdfpath = './Testfile/'#pdf文件路径
pdffile = 'test.pdf'#pdf文件名

pdf = fetchPdf(pdfpath,pdffile)
result = pdf.read()#返回一个dict
print(result)
'''
{'state': 1, 'msg': '成功', 'info': {'filename': 'test.pdf'}, 'text': {'textTitle': '', 'textString': 'pdf文件内容'}}
'''