#-*-coding: utf-8 -*-
# python str采用unicode编码，但unicode相对占用内存，因此在传输或者储存时转换为utf-8
# ord("str") 获取字符的整数表示	chr(num)将编码转换为对应字符 E.g:
print(ord('A'))
print(chr(65))

#python 的bytes数据用 b'' or b""
x = b'ABC'
print(x)

#以unicode表示的str可用encode()编码为指定的bytes E.g:
y = "ABC".encode('ascii')
print (y)
z = '中国'.encode("utf-8")  #UnicodeencodeError
print(z)

#bytes转换为str用decode() E.g:
w = b'ABC'.decode('ascii')
print (w)
# #如果bytes中有无效字节，可用errors='ignore'忽略错误字节 E.g:
a = b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore')

#计算str字符数用len() E.g:
b = 'abc'
print (len(b))
c = '中文'
print (len(c))
# #len()计算字节数 E.g:
d = b'abc'
e = '中文'.encode("utf-8")
print (len(d))
print (len(e))


#format 同c E.g:
print ("naem %s age %d" % ('shih',22) )
# #format()

