Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> var1 = 1
>>> var2 = 10
>>> print var2
10
>>> print var1
1
>>> var2 = long(var2[,base])
SyntaxError: invalid syntax
>>> print long(var2 [,base ])
SyntaxError: invalid syntax
>>> var2 = long(10[,base])
SyntaxError: invalid syntax
>>> var2 = 20
>>> print var2
20
>>> del var2
>>> print var2

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print var2
NameError: name 'var2' is not defined
>>> print var1
1
>>> chr(var2)

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    chr(var2)
NameError: name 'var2' is not defined
>>> var2 = chr(20)
>>> print var2

>>> 
