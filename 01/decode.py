#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import string

print(string.ascii_letters)
a=string.ascii_letters;
print(a[:])
#help('string')
a=b'A'
print(a)
print(ord(a))
print('a'.encode())
print(r'输出unicode编码字符编码后的结果,在编码前面加上\u,例如\u4e2d结果为''\u4e2d')
print(u'中')
print('unicode转ascii:20013--中','')
print('输出字母A的ascii',ord('A'))
print('输出字符中的10进制整数模式',ord('中'))
#print('输出字符u4e2d的ascii',ord('\u4e2d'))
print('将unicode字符还原成unicode编码，用str.encode','中'.encode('unicode-escape'))
print(b'a'=='a')
print('将unicode字符还原成utf-8编码，用str.encode','中文'.encode('utf-8'))
print('将unicode字符还原成unicode编码，用str.encode','中文'.encode('unicode-escape'))
print(0xe4)
print(b'')
#print('将unicode字符还原成ascii编码，用str.encode','中文'.encode('ascii'))
#'%s,%s' %('wangge','hello')
#格式化字符串输出，
#常见的占位符有：

#%d	整数
#%f	浮点数
#%s	字符串
#%x	十六进制整数
print('%-10s,%s' %('wangge','hello'))


#格式化整数和浮点数
print('%010d-%003d' % (1,12))
print('%05d%.10f' %(2,1.0))
print('%04.3e' %(4.5))
print('%d%%' % (1000/10))
print('%2s' % '啊')
print(str(100)+'%')

score1=72
score2=89
print(type((score2-score1)/score2))
print('分数提升百分比:%.2f%%' % ((score2-score1)/score2))

#字符串内存
a='a'
b='a'
print(a==b)
