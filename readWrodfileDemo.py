#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-01-11 17:39:38
# @Author  : 如风 (26982310@qq.com)
# @Link    : http://blog.youmaku.top
# @Version : $Id$

import os
from customTools.fetchdocx import fetchDocx

docpath = './Testfile/'#docx文件路径
docname = 'test.docx'#docx文件名称

doc = fetchDocx(docpath,docname)
result = doc.read()#返回一个dict
print(result)
'''
{'state': 1, 'msg': '成功', 'info': {'filename': 'test.docx'}, 'text': {'textTitle': 'docx文件内容第一行', 'textString': 'docx文件内容'}}
'''
