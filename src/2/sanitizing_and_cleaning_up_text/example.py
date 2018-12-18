# example.py
#
# Example of some tricky sanitization problems

# A tricky string
s = 'p\xfdt\u0125\xf6\xf1\x0cis\tawesome\r\n'
print(s)

# (a) Remapping whitespace
#ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，
# 它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常。
remap = {
    ord('\t') : ' ',
    ord('\f') : ' ',
    ord('\r') : None      # Deleted
}
#Python translate() 方法根据 maketrans() 方法给出的字符映射转换表转换字符串中的字符。
a = s.translate(remap)
print('whitespace remapped:', a)

#======================================================
# 以下实例展示了使用 maketrans() 方法加 translate() 方法将所有元音字母转换为指定的数字，并删除指定字符：
intab = "aeiou"

outtab = "12345"

deltab = "thw"

trantab1 = str.maketrans(intab, outtab)  # 创建字符映射转换表

trantab2 = str.maketrans(intab, outtab, deltab)  # 创建字符映射转换表，并删除指定字符

test = "this is string example....wow!!!"

print(test.translate(trantab1))

print(test.translate(trantab2))
#========================================================


print("=======Remove all combining characters/marks=========")
# (b) Remove all combining characters/marks
import unicodedata
import sys
print(sys.maxunicode)#  值是  1114111 则表示使用uns4标准，即：4个字节表示
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                         if unicodedata.combining(chr(c)))

# print(cmb_chrs)
b = unicodedata.normalize('NFD', a)
c = b.translate(cmb_chrs)
print('accents removed:', c)

# (c) Accent removal using I/O decoding
d = b.encode('ascii','ignore').decode('ascii')
print('accents removed via I/O:', d)
