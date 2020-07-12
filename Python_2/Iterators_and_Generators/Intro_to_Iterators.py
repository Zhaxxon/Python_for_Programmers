my_list = [1, 2, 3]
# next(my_list)
#Traceback (most recent call last):
#  File "/usercode/__ed_file.py", line 2, in <module>
# next(my_list)
#TypeError: 'list' object is not an iterator

list_iterator = iter(my_list)

print(next(list_iterator))
#1

print(next(list_iterator))
#2

print(next(list_iterator))
#3

print (next(list_iterator))
#Traceback (most recent call last):
#  File "/usercode/__ed_file.py", line 16, in <module>
# print (next(list_iterator))
#StopIteration:

for item in iter(my_list):
    print(item)

#1
#2
#3