#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time       : 2020/7/10 14:47
# @Author     : 代登辉
# @Email      : 3276336032@qq.com
# @File       : word.py
# @Software   : PyCharm
# @Description: 读取word

import docx


def getTextWord(wordFileName):
    doc = docx.Document(wordFileName)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)
