#
# *! من 1 حتى 10 # ----------------------------
# # type()
# # All Data in Python is Object
# # ----------------------------

# print(type(10))  # int => Integer
# print(type(100))  # int => Integer
# print(type(-50))  # int => Integer

# print(type(100.9))  # float => Floating Point Number
# print(type(1.950950))  # float => Floating Point Number
# print(type(-100.9595))  # float => Floating Point Number

# print(type("Hello Python"))  # str => String

# print(type([1, 2, 3, 4, 5]))  # list => List

# print(type((1, 2, 3, 4, 5)))  # tuple => Tuple

# print(type({"One": 1, "Two": 2, "Three": 3}))  # dict => Dictionary

# print(type(2 == 2))  # bool => Boolean

# x = 10
# print(x)  # int => Integer

# help ("keywords")  # help() => Help Function

# a , b , c = 10, 20, 30
# print(a, b, c)  # int => Integer

# # ----------------------------
# # Escape Sequences Characters
# # \b => Back Space
# # \newline => Escape New Line + \
# # \\ => Escape Back Slash
# # \' => Escape Single Quotes
# # \" => Escape Double Quotes
# # \n => Line Feed
# # \r => Carriage Return
# # \t => Horizontal Tab
# # \xhh => Character Hex Value
# # ----------------------------

# # Back Space
# print("Hello\bWorld")  # Will Remove o

# # Escape New Line + Back Slash
# print("Hello \
# I Love \
# Python")

# # Escape Back Slash
# print("I Love Back Slash \\")

# # Escape Single Quote
# print('I Love Single Quote \'Test\' ')

# # Escape Double Quotes
# print("I Love Double Quotes \"Test\" ")

# # Line Feed
# print("Hello World\nSecond Line")

# # Carriage Return
# print("123456\rAbcde")

# # Horizontal Tab
# print("Hello\tPython")

# # Character Hex Value
# print("\x4F\x73")

# # -------------------
# # -- Concatenation --
# # -------------------

# msg = "I Love"
# lang = "Python"
# print(msg + " " + lang)

# full = msg + " " + lang
# print(full)

# a = "First \
# Second \
# Third"

# b = "A \
# B \
# C"

# print(a + "\n" + b)

# # print("Hello " + 1)  # Error
# print(1 + 1)  # Works fine


#*! من 18 حتى 11 # ----------------------------

# s1 = "I Love Python 'test' "
# s2 = 'I Love Python "test" '
# print(s1)
# print(s2)

# s3= """ I Love Python
# hello "test" \\\ '+'
# World """
# print(s3)

# s1= "I Love Python"
# print(s1[0])  # I
# print(s1[8])  # L
# print(s1[3:11])  # ve Python
# print(s1[::3])  
# print(s1[:-5:-1])  

# s1= "I Love Python"
# s2= "  I Love Python   "
# print(len(s1))  # 13
# print(len(s2))  # 18

# s2= "  I Love Python   "
# print(s2.strip())  # I Love Python
# print(s2.lstrip())  #   I Love Python   
# print(s2.rstrip())  #   I Love Python   
# s3= "@##@##@# I Love Python @##@#@"
# print(s3.strip("#@"))  # I Love Python
# name= "akram 3d 5g"
# print(name.capitalize())
# print(name.title())  
# print(name.upper())  
# print(name.lower())  

# a , b , c , d = "1", "10", "100", "1000"
# print(a.zfill(4) + "\n" + b.zfill(4) + "\n" + c.zfill(4) + "\n" + d.zfill(4))  # 001 010 100 1000

# a= "I Love Python and Php and MySQL"
# print(a.split())  # ['I', 'Love', 'Python', 'and', 'Php', 'and', 'MySQL']
# a= "I-Love-Python-and-Php-and-MySQL"
# print(a.split("-"))  # ['I', 'Love', 'Python', 'and', 'Php', 'and', 'MySQL']
# a= "I-Love-Python-and-Php-and-MySQL"
# print(a.split("-",2))  
# a= "I-Love-Python-and-Php-and-MySQL"
# print(a.rsplit("-",3)) 

# e = "akram"
# print(e.center(9,"#"))  #  ##akram##

# f = " i love python and php and mysql because php os easy "
# print(f.count("php"))  # 2 i love python and java and mysql because java os easy
# print(f.count("php",10,25))  # 2 i love python and java and mysql because java os easy

# g = " i love python and php and mysql because php is easy "
# print(g.swapcase())  # 19

# s = "i love python"
# print(s.startswith("i"))  # True
# print(s.endswith("n"))  # True
# print(s.endswith("o",1,4))  # True
# print(s.startswith("v",-9))

# s = "i love python"
# print(s.find("o",5,10))  # 6
# print(s.index("o"))  # 6
# print(s.index("o",5,10))  # 6
# n = "akram123"
# print(n.isalpha())  # True
# print(n.isalnum())  # True
# print(n.ljust(10, "#"))  # akram123##
# print(n.rjust(10, "#"))  # ##akram123

# s="i love\tpython and\tphp and mysql\tbecause php is easy"
# print(s.expandtabs(2))  # i love    python and    php and mysql    because php is easy
# s1="""i love
# "python and php
# and mysql
#  because
# php is easy"""
# print(s1.splitlines())  # ['i love', '"python and php', 'and mysql', ' because', 'php is easy']

# s= "ak123"
# s1= "ak--13"
# print(s.isidentifier())
# print(s1.isidentifier()) 

# s1 = " hello one two three one one one " 
# print(s1.replace("one", "1"))  #  hello 1 two three 1 1 1
# print(s1.replace("one", "1",2))  #  hello 1 two three 1 one one

# l = ["akram", "ahmed", "123"]
# print("".join(l))  
# print("-".join(l))  # akram-ahmed-123
# print(",".join(l)) 

# n = "akram"
# l="python"
# y=30
# print("Hello my name is : %s I Love %s and I Have %d  Years Old" %(n,l,y))# Hello akram I Love python and I Have 30 Years Old
# print("I Have %.2f  Years Old" %(y))
# print("Hello my name is : %.2s " %(n))
# print("My old is : {:.2f}".format(y))

# a , b , c = 10, 20, 30
# print("{2} {0}  {1} ".format(a,b,c))
# print(f"{c:.2f} {a:.3f}  {b:.5f} ")
# print("Hello my name is : {} I Love {} and I Have {}  Years Old".format(n,l,y))
# print(f"Hello my name is : {n} I Love {l} and I Have {y}  Years Old")

#*! من 23 حتى 21 # ----------------------------

# l = ["akram", "ahmed", "@" ,1 ,2 , True , False , 10.5 , 20.5]
# print(l)  # ['akram', 'ahmed', '@', 1, 2, True, False, 10.5, 20.5]
# print(type(l))  # <class 'list'>
# print(type(l[-1]))  # <class 'list'>
# print(l[1:4])  
# print(l[4:])  
# l[0:3]=["A"]
# print(l)

# l = ["akram", "@" ,1, False , 10.5 , 20.5]
# l.append("python")
# print(l)  # ['akram', 'ahmed', '@', 1,
# l2 = ["ahmed", "python", 2, True , 30.5 , 40.5]
# l.append(l2)
# print(l)  # ['akram', 'ahmed', '@', 1, False
# print(l[7][1])  # python

# l.extend(l2)
# print(l)  # ['akram', 'ahmed', '@', 1, False
# l.insert(1, "insert")
# print(l)  # ['akram', 'insert', 'ahmed', '@', 1, False
# l.remove("insert")
# print(l)  # ['akram', 'ahmed', '@', 1, False
# l3 = l.pop(1)
# print(l3)  # ahmed
# print(l)  # ['akram', '@', 1, False
# a=[1,-8,2,3,4,-5,6,-7,1]
# a.sort()
# print(a)  
# a.sort(reverse=True)
# print(a)
# print(a.count(1))  # 2
# print(len(a))  # 1
# a.reverse()
# print(a)  # [-7, -5, -8, 1, 1, 2, 3, 4, 6]
# b=a.copy()
# a.clear()
# print(a)  # []
# print(b)  # [-7, -5, -8, 1, 1, 2, 3, 4, 6]

# l = ["akram", "ahmed", "@" ,1 ,2 , True , False , 10.5 , 20.5]
# print(l.pop(1))  # ahmed
# print(l)  # ['akram', 'ahmed', '@', 1, 2, True, False, 10.5, 20.5]


#*! من 25 حتى 24 # ----------------------------

# t1 = ("Html", "CSS", "JS", "Python")
# t2 = "Html", "CSS", "JS", "Python"
# print(t1)  # ('Html', 'CSS', 'JS', 'Python')
# print(t2)  # ('Html', 'CSS', 'JS', 'Python')
# print(type(t1))  # <class 'tuple'>
# print(type(t2))  # <class 'tuple'>
# print(t2[-1])  

# a = (1,2,3)
# b = (4,8)
# c = a +(9,11,'akram') + b
# print(c)

# t=(1,2)
# l=[5,7]
# s="akram"
# print(t * 3)
# print(l * 3)
# print(s * 3)

# a = ('a','c',4,'w')
# x,y , _ ,z = a
# print(x,y,z)

#*! من 32 حتى 26 # ----------------------------
