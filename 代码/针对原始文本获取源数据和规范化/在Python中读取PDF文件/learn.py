#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time       : 2020/7/3 19:07
# @Author     : 代登辉
# @Email      : 3276336032@qq.com
# @File       : learn.py
# @Software   : PyCharm
# @Description: 方法描述,必填
from PyPDF2 import PdfFileWriter, PdfFileReader

writer = PdfFileWriter()
reader = PdfFileReader(open("E:\\课程\\自然语言处理\\代码\\针对原始文本获取源数据和规范化\\在Python中读取PDF文件\\pdf\\虚拟内存.pdf", "rb"))
print(reader.getPage(0))
print(reader.getPage(0).extractText())