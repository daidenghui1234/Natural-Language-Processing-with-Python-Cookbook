#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time       : 2020/7/3 17:54
# @Author     : 代登辉
# @Email      : 3276336032@qq.com
# @File       : pdf.py
# @Software   : PyCharm
# @Description: 读取pdf文件

from PyPDF2 import PdfFileReader


def getTextPDF(pdfFileName, password=''):
    pdf_file = open(pdfFileName, 'rb')
    read_pdf = PdfFileReader(pdf_file)
    if password != '':
        read_pdf.decrypt(password)
    text = []
    for i in range(0,read_pdf.getNumPages()):
        text.append(read_pdf.getPage(i).extractText())
    return '\n'.join(text)
