#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time       : 2020/7/10 19:10
# @Author     : 代登辉
# @Email      : 3276336032@qq.com
# @File       : creatCorpus.py
# @Software   : PyCharm
# @Description: 创建语料库

import os
from 在python中读取word文件 import word   # 导入自定义库
from 在Python中读取PDF文件 import pdf
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
import nltk

def getText(textFileName):
    #  读取txt文档
    file = open(textFileName)
    return file.read()


# 创建文件夹
newCorpusDir = 'mycorpus/'
if not os.path.isdir(newCorpusDir):
    os.mkdir(newCorpusDir)
# 读取文件
txt1 = getText('sample_feed.txt')
txt2 = pdf.getTextPDF('sample-pdf.pdf')
txt3 = word.getTextWord('sample-one-line.docx')

files = [txt1, txt2, txt3]
for idx, f in enumerate(files):
    with open(newCorpusDir+str(idx)+'.txt', 'w') as fout:
        fout.write(f)

newCorpus = PlaintextCorpusReader(newCorpusDir, '.*')

print(newCorpus.words()[:20])
print(newCorpus.sents(newCorpus.fileids()[1]))
print(newCorpus.paras(newCorpus.fileids()[0]))
print(newCorpus.fileids())
print(newCorpus.words(['1.txt', '2.txt']))
word = newCorpus.words(['0.txt'])
fDist = nltk.FreqDist(word)
print(fDist.most_common(10))

