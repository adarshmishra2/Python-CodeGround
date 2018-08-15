Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> age=14
>>> age
14
>>> print("hello world!")
hello world!
>>> 
=============================== RESTART: Shell ===============================
>>> myname ="adarsh"
>>> firname = "ada"
>>> secname = "rsh"
>>> fullname = firname + secname
>>> fullname
'adarsh'
>>> fullname = firname + " " + secname
>>> fullname
'ada rsh'
>>> random = "adarshshcsbvjhsbvsvbshssdcvsc"
>>> random[0,6]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    random[0,6]
TypeError: string indices must be integers
>>> random[10]
'b'
>>> random[0:6]
'adarsh'
>>> random[0:3]
'ada'
>>> random[3:]
'rshshcsbvjhsbvsvbshssdcvsc'
>>> print (%s adarsh %("hello"))
SyntaxError: invalid syntax
>>> print ("%s adarsh" %("hello"))
hello adarsh
>>> print ("my name is %s and my age is %d" %("adarsh",21))
my name is adarsh and my age is 21
>>> print ("hello %s %s" %("adarsh","mishra"))
hello adarsh mishra
>>> shoppinglist = ["milk","carrot","apples","icecream"]
>>> shoppinglist[2]
'apples'
>>> shoppinglist[0]
'milk'
>>> shoppinglist[2]=["chocolate"]
>>> shoppinglist
['milk', 'carrot', ['chocolate'], 'icecream']
>>> shoppinglist[2]="chocolate"
>>> shoppinglist
['milk', 'carrot', 'chocolate', 'icecream']
>>> shoppinglist[2]='chocolate'
>>> shoppinglist
['milk', 'carrot', 'chocolate', 'icecream']
>>> shoppinglist[4]="apples"
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    shoppinglist[4]="apples"
IndexError: list assignment index out of range
>>> shoppinglist = shoppinglist + shoppinglist[4]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    shoppinglist = shoppinglist + shoppinglist[4]
IndexError: list index out of range
>>> del shoppinglist[0]
>>> shoppinglist
['carrot', 'chocolate', 'icecream']
>>> shoppinglist.insert(2,"apples")
>>> shoppinglist
['carrot', 'chocolate', 'apples', 'icecream']
>>> shoppinglist.remove(2)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    shoppinglist.remove(2)
ValueError: list.remove(x): x not in list
>>> shoppinglist.remove("apples")
>>> shoppinglist
['carrot', 'chocolate', 'icecream']
>>> arr1 = [23,25,54]
>>> arr2 = [21,24]
>>> arr3 = arr1 + arr2
>>> arr3
[23, 25, 54, 21, 24]
>>> len(shoppinglist)
3
>>> max(arr3)
54
>>> min(arr3)
21
>>> max(shoppinglist)
'icecream'
>>> shoppinglist.append("brocolli")
>>> shoppinglist
['carrot', 'chocolate', 'icecream', 'brocolli']
>>> shoppinglist.count("icecream")
1
>>> shoppinglist.insert("apples")
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    shoppinglist.insert("apples")
TypeError: insert() takes exactly 2 arguments (1 given)
>>> 
=============================== RESTART: Shell ===============================
>>> student = {"eric":14,"tina":32,"rohan":23,"mohit":11}
>>> student["rohan"]
23
>>> student["eric"]=15
>>> student["eric"]
15
>>> student
{'rohan': 23, 'tina': 32, 'mohit': 11, 'eric': 15}
>>> del student["eric"]
>>> studeny
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    studeny
NameError: name 'studeny' is not defined
>>> student
{'rohan': 23, 'tina': 32, 'mohit': 11}
>>> student.clear()
>>> student
{}
>>> del student
>>> student
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    student
NameError: name 'student' is not defined
>>> student = {"eric":14,"tina":32,"rohan":23,"mohit":11}
>>> student
{'rohan': 23, 'tina': 32, 'mohit': 11, 'eric': 14}
>>> len(student)
4
>>> student.key()
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    student.key()
AttributeError: 'dict' object has no attribute 'key'
>>> student.keys()
dict_keys(['rohan', 'tina', 'mohit', 'eric'])
>>> student.values()
dict_values([23, 32, 11, 14])
>>> student2 = {"eric":14,"tina":32,"rohan":23,"mohit":11}
>>> student.update(student2)
>>> student2
{'rohan': 23, 'tina': 32, 'mohit': 11, 'eric': 14}
>>> student
{'rohan': 23, 'mohit': 11, 'eric': 14, 'tina': 32}
>>> student2 = {"erics":14,"tinas":32,"rohani":23,"mohitd":11}
>>> student.update(student2)
>>> student
{'rohan': 23, 'mohit': 11, 'eric': 14, 'mohitd': 11, 'tina': 32, 'rohani': 23, 'tinas': 32, 'erics': 14}
>>> 
