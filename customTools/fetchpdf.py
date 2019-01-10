#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-01-10 11:57:26
# @Author  : 如风 (26982310@qq.com)
# @Link    : http://blog.youmaku.top
# @Version : $Id$
import os
import sys
import importlib
from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed


class fetchPdf(object):
    """
    读取PDF文件
    filepath:文件路径
    filename:文件名称
    """
    def __init__(self, filepath,filename):
        super(fetchPdf, self).__init__()
        self.filepath = filepath
        self.filename = filename
        self.path = os.path.join(filepath,filename)

    def read(self):
        '''读取docx文件的内容'''
        textTitle = ''
        textString = ''
        state = 0
        msg = ''
        info = dict(filename=self.filename)
        text={}
        if self.__extension(self.filename):
            try:
                fp = open(self.path, 'rb') # 以二进制读模式打开
                #用文件对象来创建一个pdf文档分析器
                praser = PDFParser(fp)
                # 创建一个PDF文档
                doc = PDFDocument()
                # 连接分析器 与文档对象
                praser.set_document(doc)
                doc.set_parser(praser)

                # 提供初始化密码
                # 如果没有密码 就创建一个空的字符串
                doc.initialize()
                # 检测文档是否提供txt转换，不提供就忽略
                if not doc.is_extractable:
                    raise PDFTextExtractionNotAllowed
                else:
                    # 创建PDf 资源管理器 来管理共享资源
                    rsrcmgr = PDFResourceManager()
                    # 创建一个PDF设备对象
                    laparams = LAParams()
                    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
                    # 创建一个PDF解释器对象
                    interpreter = PDFPageInterpreter(rsrcmgr, device)

                    # 循环遍历列表，每次处理一个page的内容
                    for page in doc.get_pages(): # doc.get_pages() 获取page列表
                        interpreter.process_page(page)
                        # 接受该页面的LTPage对象
                        layout = device.get_result()
                        # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等 想要获取文本就获得对象的text属性，
                        for x in layout:
                            if (isinstance(x, LTTextBoxHorizontal)):
                                textString += x.get_text().strip()
                state = 1
                msg = '成功'            
                text = dict(textTitle=textTitle,textString=textString)
                return dict(state=state,msg=msg,info=info,text=text)
            except Exception as e:
                msg = '错误:%s' % e
                return dict(state=state,msg=msg,info=info,text=text)
        else:
            msg = '错误:文件格式无效!'
            return dict(state=state,msg=msg,info=info,text=text)

    def __extension(self,filename):
        name,extension=os.path.splitext(filename)
        return extension.lower().startswith('.pdf')
