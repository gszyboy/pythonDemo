#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-01-11 08:51:47
# @Author  : 如风 (26982310@qq.com)
# @Link    : http://blog.youmaku.top
# @Version : $Id$
import os
from win32com import client
'''
className:Doc2Docx
doc转docx
'''
class Doc2Docx(object):
    """
    doc转docx
    filepath:文件路径
    filename:文件名称
    """
    def __init__(self, filepath,filename):
        super(Doc2Docx, self).__init__()
        self.path = os.path.join(filepath,filename)
        self.filepath = filepath
        self.filename = filename

    def tConversion(self):
        '''转换doc文件'''
        try:
            #调用word程序
            word = client.Dispatch('Word.Application')
            #DispatchEx:独立进程
            #word = client.DispatchEx('Word.Application')
            #不在前台显示文档及错误，在实际使用阶段可以全部关闭，提高运行速度，但是
            #在调试时打开还是用处挺大的，可以对操作是否实现自己的需求进行直观的判断。
            word.Visible = 0
            word.DisplayAlerts = 0

            doc = word.Documents.Open(self.path)

            #使用参数16表示将doc转换成docx
            #保存在原路径下面,文件名是在原文件名后面加.docx
            doc.SaveAs(self.path + '.docx',16)

            tempname = doc.__str__()

            doc.Close()
            word.Quit()
            return dict(filepath=self.filepath,filename=tempname)
        except Exception as e:
            raise e

    def __file_extension(self,path=None,choose=1):
        '''
        获取文件名或者扩展名的方法
        path:带有扩展名的原始文件名称
        choose:0,文件名;1,文件扩展名
        '''
        path = (path if path != None else self.filename)
        if int(choose) == 0: 
            return os.path.splitext(path)[0]
        else:
            return os.path.splitext(path)[1]
