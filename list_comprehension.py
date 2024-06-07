# -*- coding:utf-8 -*-
# software: PyCharm
# datetime:2024/5/26 20:56
# @Author: yuhuifei
"""
问：请解释什么是列表推导式（list comprehension），并举例说明其用法
答：（comprehensions）是一种简洁而强大的语法，用于从已存在的数据（列表、元组、集合、字典等）中创建新的数据结构。推导式包括：
列表推导式
元组推导式
字典推导式
集合推导式

语法格式: expression for item in iterable if condition
"""
from math import pi

# 列表推导式
list_1 = [(x, y) for x in [1, 2, 3] for y in [3, 4, 5] if x != y]
list_2 = [x for x in range(10) if x % 2 == 0]  # 筛选偶数
word_list = ['expression', 'hi', 'item', 'for', 'it', 'condition']
list_3 = [word for word in word_list if len(word) >= 3]
list_4 = [word.upper() for word in word_list]
list_5 = [x ** 2 for x in range(10)]
list_6 = [char for char in 'comprehension']
list_7 = [[x * j for j in range(1, 4)] for x in range(1, 5)]
list_8 = [str(round(pi, n)) for n in range(1, 6)]
print(list_1)
print(list_2)
print(list_3)
print(list_4)
print(list_5)
print(list_6)
print(list_7)
print(list_8)
