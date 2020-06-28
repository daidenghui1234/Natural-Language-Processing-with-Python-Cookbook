#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 20:36
# @Author  : 代登辉
# @Email   : 3276336032@qq.com
# @File    : external_corpus.py
# @Software: PyCharm

from nltk.corpus import CategorizedBracketParseCorpusReader
from random import randint

# 读取文件
reader = CategorizedBracketParseCorpusReader(r'E:/课程/自然语言处理/代码/语料库和WordNet/加载并访问外部语料库/tokens/neg',
                                             r'.*\txt', cat_pattern=r'(\w)/*')
print(reader.categories())
print(reader.fileids())

posFiles = reader.fileids(categories='pos')
negFiles = reader.fileids(categories='neg')
