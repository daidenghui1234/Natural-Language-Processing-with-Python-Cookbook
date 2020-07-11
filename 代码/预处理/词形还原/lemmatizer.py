#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time       : 2020/7/11 18:02
# @Author     : 代登辉
# @Email      : 3276336032@qq.com
# @File       : lemmatizer.py
# @Software   : PyCharm
# @Description: WordnetLemmatizer函数的使用

from nltk import word_tokenize, PorterStemmer, WordNetLemmatizer
raw = "My name is Maximus Decimus Meridius, commander of the armies of the north, General of the Felix legions and " \
      "loyal servant to the true emperor, Marcus Aurelius. Father to a murdered son, husband to a murdered wife. And " \
      "I will have my vengeance, in this life or the next. "
tokens = word_tokenize(raw)

porter = PorterStemmer()
stems = [porter.stem(t) for t in tokens]
print(stems)
# 词形还原能够判断专有名词，其不需要去除后缀's'，但是对于非专有名词（如：legions, armies）来说需要去除而非替换其后缀
# 词形还原是一个字典匹配的过程。
lemmatizer = WordNetLemmatizer()
lemmas = [lemmatizer.lemmatize(t) for t in tokens]
print(lemmas)

