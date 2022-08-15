# -*- coding: utf-8 -*-

#定義函數去除空白
def trim(s):
  #條件取字串位置1前面不包含1是空白,字串取位置1含1全部.
	while s[:1]==' ':
		s=s[1:]
  #條件取字串位置-1是空白,字串取位置-1含-1全部.
	while s[-1:]==' ':
		s=s[:-1]
	return s
# 測試去除空白
if trim('hello  ') != 'hello':
    print('測試失败!')
elif trim('  hello') != 'hello':
    print('測試失败!')
elif trim('  hello  ') != 'hello':
    print('測試失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('測試失败!')
elif trim('') != '':
    print('測試失败!')
elif trim('    ') != '':
    print('測試失败!')
else:
    print('測試成功!')
