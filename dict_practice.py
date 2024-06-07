"""
字典类型是python内置的一种数据类型，可变，可以存储任意类型的对象。
以键值对方式存储，通过键来访问。
"""

# 定义方式1
dict1 = {'ykx': 'yukexin', 'yhf': 'yuhuifei', 'age': 35}
# 定义方式2
dict2 = dict(ykx='yukexin', yhf='yuhuifei', age=35)

# 访问值
ykx = dict1['ykx']  # 方式1
yhf = dict2.get('yhf')  # 方式2
no_key = dict2.get('no_key', 'default_value')  # 方式3:找不到对应key，则给默认值
print(ykx)
print(yhf)
print(no_key)

# 修改值
dict1['yhf'] = 'rename'
print(dict1['yhf'])

# 添加键值对
dict1['add_key'] = 'add_value'
print(dict1['add_key'])

# 删除键值对
del_value = dict1.pop('add_key')
print(del_value)
print(dict1)

del dict2['yhf']
print(dict2)

# 遍历键值对
for key, value in dict1.items():
    print(f'key={key},value={value}')

# 遍历key
for key in dict1.keys():
    print(f'key={key}')

# 遍历value
for value in dict1.values():
    print(f'value={value}')

# 拷贝字典
dict3 = dict1.copy()
print(f'dict3={dict3}')

