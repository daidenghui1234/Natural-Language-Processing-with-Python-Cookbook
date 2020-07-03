#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time       : 2020/7/3 18:33
# @Author     : 代登辉
# @Email      : 3276336032@qq.com
# @File       : TestPDFs.py
# @Software   : PyCharm
# @Description: 读取pdf文件

import pdf

pdfFile = 'sample-one-line.pdf'
pdfFileEncrypted = 'sample-one-line.protected.pdf'

print('PDF 1: \n', pdf.getTextPDF(pdfFile))
print('PDF 2: \n', pdf.getTextPDF(pdfFileEncrypted, 'tuffy'))