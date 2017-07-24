
import math
import sys

print(sys.version)
#none
print(None)

#整数
print ("哈哈")
print("带有r的换行:")
a=1;
b=44444444444444444;
c=0x1f
print(a,b,c)


#浮点数
d=1.2e-5
print(0.11100010010000000 * ( 2 ^ 16 ))
print(d-2);
#地板除
print('0/3=',0/3)
print('3/3=',3/3)
print('1/3=',1/3)
print('1/2=',1/2)
print('2.8//3=',2.8//3)
print(math.floor(2.8//3))
#精确除法 
print('1.8/3=',1.8/3)
print('3.3//1.1=',3.3//1.1)
print('3.3/1.1=',3.3/1.1)
print('2.8/3=',2.8/3)
print('2.8/3.0=',2.8/3.0)

#字符串
#字符串 前面 加上r默认不转义
print(r"i'm ok !\"")
print(r"\\")
print('不带有r的换行')
print('''得到的
aaaa
ddddd
ddddd\n\\''')

print('带有r的换行:')
print(r'''得到的
aaaa
ddddd
ddddd\n\\
''')

#逗号会把分开的 字符串连接起来
print("a","b","c")

a='abcd\aefg'
print(a)
print(len(a))
print(a[4:5])
print(ord(a[4:5]))
print(a[5:6])




# 布尔值运算,逻辑运算
print('True or False:'+str(True or False))
print('1:'+str(1))
sep='-'
print(sep.join('abc'))
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85} 
print(1 and 4)
print("0 or 4:"+str(0 or 4))
print(1 & 4)


#常量
print("PI:",3.14)