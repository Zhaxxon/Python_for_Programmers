# Python 2
x = 'blah'
print (type(x))
#str

y = u'blah'
print (type(y))
#unicode


# Python 3
x = 'blah'
print (type(x))
#<class 'str'>

y = u'blah'
print (type(y) )
#<class 'str'>


# Python 2
print ('abcdef' + chr(255))
#'abcdef\xff'


# Python 3
print (('abcdef' + chr(255)).encode('utf-8'))
#b'abcdef\xc3\xbf'


# Python 2
unicode('abcdef' + chr(255))

#Traceback (most recent call last):
#  File "/usercode/__ed_file.py", line 2, in <module>
#    unicode('abcdef' + chr(255))
#UnicodeDecodeError: 'ascii' codec can't decode byte 0xff in position 6: ordinal not in range(128)