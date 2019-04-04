# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#variabel
c = 7
d = "Tomy Prawoto"

print(c)
print(d)

#integer
x = 4
y = 6969787819
z = -456283

print(type(x))
print(type(y))
print(type(z))

#float
x = 1.115
y = 1.5
z = -35.60

print(type(x))
print(type(y))
print(type(z))

#complex
x = 5+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#variabel string
a = "Hello, World!"
print(a[1])

b = "Hello, World!"
print(b[2:7])

a = "Hello, World!"
print(a.strip())

a = "Hello, World!"
print(len(a))

a = "Hello, World!"
print(a.lower())

a = "Hello, World!"
print(a.upper())

#variabel boolean
a = 40
b = 300
if b>a:
    print("b lebih besar dari a")

#input output
npm = input()
print(npm)

#operator
x = 5
y = 3

print(x+y)

x = 5
y = 3

print(x-y)

x = 12
y = 3

print(x*y)

x = 8
y = 2

print(x/y)

x = 5
y = 2

print(x%y)

#perulangan for
ulang = ["Motor","Mobil","Pesawat"]
for i in range(ulang):
    print(i)
    
#perulangan while
coba = 1
while i < 6 :
    print(i)
    i += 1
    
#if
a = 40
b = 300
if b > a :
    print("b lebih besar dari a")

#elif
a = 40
b = 40
if b > a :
    print("b besar dari a")
elif a ==b :
    print("a sama dengan b")
    
#else
a = 300
b = 40
if b > a :
    print("b besar dari a")
elif a == b :
    print("a sama dengan b")
else :
    print("a lebih dari b")
    
#try except
x = 0
y = "1"
try :
    z = x + y
    print(z)
except TypeError :
    print("Perbedaan data")
            