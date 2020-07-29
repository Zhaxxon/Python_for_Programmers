import hashlib
md5 = hashlib.md5()
md5.update('Python rocks!')
#Traceback (most recent call last):
#  File "/usercode/__ed_file.py", line 3, in <module>
#    md5.update('Python rocks!')
#TypeError: Unicode-objects must be encoded before hashing


import hashlib
md5 = hashlib.md5()

md5.update(b'Python rocks!')
print (md5.digest())
#b'\x14\x82\xec\x1b#d\xf6N}\x16*+[\x16\xf4w'


import hashlib
sha = hashlib.sha1(b'Hello Python').hexdigest()
print (sha)
#'422fbfbc67fe17c86642c5eaaa48f8b670cbed1b'