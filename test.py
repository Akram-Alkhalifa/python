# # # name = "Elzero"
# # # name1 = "#@#@Elzero#@#@"
# # # print(name[1])
# # # print(name[2])
# # # print(name[-1])
# # # print(name[1:4])
# # # print(name[0:5:2])
# # # print(name[-2::-2])
# # # print(name.strip("#@"))
# # # num = "9"
# # # num = "15"
# # # num = "130"
# # # num = "950"
# # # # num = "1500"
# # # print(num.zfill(4))

# # name_one = "Osama"
# # name_two = "Osama_Elzero"

# # print(name_one.rjust(20, "@"))
# # print(name_two.rjust(20, "@"))
# # name_one = "OSamA"
# # name_two = "osaMA"
# # print(name_one.swapcase())
# # print(name_two.swapcase())
# # msg = "I Love Python And Although Love Elzero Web School"
# # print(msg.count("Love"))
# # name = "Elzero"

# # print(name.index("z"))

# msg = "I <3 Python And Although <3 Elzero Web School"
# print(msg.replace("<3", "Love",1))

# name = "Osama"
# age = 38
# country = "Egypt"

# print(f"My Name Is {name}, And My Age Is {age}, And My Country Is {country}")


# x=1+2j
# print(x.imag)
# print(x.real)
# # Print Imaginary Part Here
# # Print Real Part Here

# num = 10
# print("{:.10f}".format(num))  # 10.0000000000
# print(f"{num:.10f}")  # 10.0000000000
# # Needed Ouput
# # 10.0000000000


# num = 159.650
# print(int(num))
# print(type(int(num)))
# # Needed Output
# # 159
# # <class 'int'>


# x = 100 - 115 
# y = 50 * 30 
# z = 21 % 4
# w = 110 // 11 
# v =97 // 20 
# print(x)
# print(y)
# print(z)
# print(w)    
# print(v)


# friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
# print(friends[0::2])  # Osama
# print(friends[1::2])  # Osama

# friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
# friends[-1] = "Elzero"
# friends[-2] = "Elzero"
# print(friends)
# # Needed Output
# # ["Osama", "Ahmed", "Sayed", "Elzero", "Elzero"]

# friends = ["Osama", "Ahmed", "Sayed"]
# friends.append("Nasser")
# friends.insert(0, "ak")
# print(friends)

# friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
# friends.remove("Nasser")
# friends.remove("Osama")
# print(friends)
# friends.pop(-1)
# print(friends)
# # Needed Output
# # ["Ahmed", "Sayed", "Salem"]
# # ["Ahmed", "Sayed"]

# friends = ["Ahmed", "Sayed"]
# employees = ["Samah", "Eman"]
# school = ["Ramy", "Shady"]
# l=friends + employees + school
# friends.extend(employees)
# friends.extend(school)
# print(friends)
# print(l)
# # Needed Output
# # ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

# friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
# friends.sort()
# print(friends)
# friends.sort(reverse=True)
# print(friends)
# print(len(friends))


# t1 = ["Html", "CSS", "JS", "Python"]
# t2 = ["Django", "Flask", "Web"]
# t1.append(t2)
# print(t1)  # ['Html', 'CSS', 'JS', 'Python', ['
# print(t1[4][0])  # Django
# print(t1[4][2])  # Django


# friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
# print(friends[1:4])  # ["Ahmed", "Sayed", "Ali"]
# print(friends[-1:-3:-1])  # ["Ali", "Sayed"]
# print(friends[-2:])  # ["Ali", "Sayed"]
# # Needed Output
# # "Ahmed", "Sayed", "Ali",
# # "Ali", "Mahmoud"

# t="ak",
# print(t)
# print(type(t))  # <class 'tuple'>

# friends = ("Osama", "Ahmed", "Sayed")
# friends = list(friends)
# friends[0] = "Elzero"
# friends = tuple(friends)
# print(friends)  # ("Elzero", "Ahmed", "Sayed")
# print(type(friends))  # <class 'tuple'> 
# print(len(friends))  # 3 Elements
# # Needed Output
# # ("Elzero", "Ahmed", "Sayed")
# # <class 'tuple'>
# # 3 Elements


# nums = (1, 2, 3)
# letters = ("A", "B", "C")
# t = nums + letters
# print(t)  # (1, 2, 3, 'A', 'B
# print(len(t))


# my_tuple = (17, 88, "a", 4)
# a,b,c,_=my_tuple
# print(a)
# print(b)
# print(c)
# print(a,b,c)
