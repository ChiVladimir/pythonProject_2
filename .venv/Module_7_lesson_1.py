# Введение. Строки байты и кодировки
from idlelib.browser import browseable_extension_blocklist

print("Hello!") #ASCII - 128 symbols
print(ord('a'))
print(ord('A'))
print(ord('H'))
print(ord('e'))
print(ord('l'))
print(ord('o'))
print(ord('!'))

a = "Hello!"
chars=[]
for i in a:
    ord(i)
    chars.append(ord(i))
print(chars)

s = ''
for i in chars:
    s +=chr(i)
print(s)

# for i in range(128): #ASCII - 128 symbols
#     print(chr(i), ' = ', ord(chr(i)))

# for i in range(1000, 1200): #UniCode - about 150 000 symbols
#     print(chr(i), ' = ', ord(chr(i)))

# for i in range(128): #bytes
#      print(chr(i), ' = ', hex(ord(chr(i))))

print(hex(ord('H')))
bb = b'0x48'
print(bb.decode())

