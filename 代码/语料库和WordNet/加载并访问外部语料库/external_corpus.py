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
reader = CategorizedBracketParseCorpusReader(r'F:/Downloads/NLP文件/mix20_rand700_tokens_cleaned/tokens',
                                             r'.*\.txt', cat_pattern=r'(\w+)/*')
print(reader.categories())
print(reader.fileids())

negFiles = reader.fileids(categories=['neg'])

fileN = negFiles[randint(0, len(negFiles)-1)]
print(fileN)

for w in reader.words(fileN):
    print(w + ' ', end=" ")
    if w is '.':
        print()
