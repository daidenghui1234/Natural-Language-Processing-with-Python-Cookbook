#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time       : 2020/7/11 17:50
# @Author     : 代登辉
# @Email      : 3276336032@qq.com
# @File       : stemmers.py
# @Software   : PyCharm
# @Description: 词干提取

from nltk import PorterStemmer, LancasterStemmer, word_tokenize

raw = "My name is Maximus Decimus Meridius, commander of the Armies of the North, General of the Felix Legions and " \
      "loyal servant to the true emperor, Marcus Aurelius. Father to a murdered son, husband to a murdered wife. And " \
      "I will have my vengeance, in this life or the next. "
tokens = word_tokenize(raw)     # 根据单词分词
porter = PorterStemmer()        # 相对少去后缀
pStems = [porter.stem(t) for t in tokens]    # 后缀（s es e ed al）
print(pStems)

lancaster = LancasterStemmer()      # 更彻底
lStems = [lancaster.stem(t) for t in tokens]    # 去除单词的大小写和后缀
print(lStems)