# Python2
u"\xa0".decode("ascii")

#Traceback (most recent call last):
#   File "/usercode/__ed_file.py", line 1, in <module>
#    u"\xa0".decode("ascii")
#UnicodeEncodeError: 'ascii' codec can't encode character u'\xa0' in position 0: ordinal not in range(128)


# Python3
u"\xa0".decode("ascii")
#Traceback (most recent call last):
#  File "/usercode/__ed_file.py", line 1, in <module>
# u"\xa0".decode("ascii")
#AttributeError: 'str' object has no attribute 'decode'


b"\xa0".decode("ascii")
#Traceback (most recent call last):
#  File "/usercode/__ed_file.py", line 1, in <module>
# b"\xa0".decode("ascii")
#UnicodeDecodeError: 'ascii' codec can't decode byte 0xa0 in position


u = chr(40960) + 'abcd' + chr(1972)
print (u.encode('utf-8'))
#b'\xea\x80\x80abcd\xde\xb4'

print (u.encode('ascii'))
#Traceback (most recent call last):
#  File "/usercode/__ed_file.py", line 5, in <module>
# print (u.encode('ascii'))
#UnicodeEncodeError: 'ascii' codec can't encode character '\ua000' in position 0: ordinal not in range(128)


u = chr(40960) + 'abcd' + chr(1972)

print (u.encode('ascii', 'ignore'))
#b'abcd'

print (u.encode('ascii', 'replace'))
#b'?abcd?'