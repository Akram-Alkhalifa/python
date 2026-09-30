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

# my_list = [1, 2, 3, 3, 4, 5, 1]
# unique_list=list(set(my_list))
# print(unique_list)
# print(type(unique_list))
# print(unique_list[:-1])
# print(*unique_list[:-1], sep=", ")
# print(*unique_list , sep=" , ")


# nums = {1, 2, 3}
# letters = {"A", "B", "C"}
# x = nums | letters
# print(x)
# z = nums.union(letters)
# print(x)
# c = nums.update(letters)
# print(x)

# v = {*nums, *letters}
# print(v)

# s={1,2,3}
# print(s)
# s.clear()
# print(s)
# s.update(["A", "B"])
# print(s)
# print(s)
# s.discard("c")
# print(s)


# set_one = {1, 2, 3}
# set_two = {1, 2, 3, 4, 5, 6}

# print(set_two.issuperset(set_one))


# d={
#     "s1":"HTML Progress Is 90%",
#     "s2":  "CSS Progress Is 80%",
#     "s3":  "Python Progress Is 30%"
# }
# print(d)
# print(d.values())
# d.update({"s4":"AI Progress Is 20%"})
# print(d)

# # 1. إنشاء الـ Dictionary
# skills = {
#     "HTML": "90%",
#     "CSS": "80%",
#     "Python": "30%"
# }

# # تحويل المفاتيح إلى قائمة للوصول إليها بالفهرس (Index)
# k = list(skills.keys())

# # 2. طباعة المهارات الثلاث بدون Loop
# print(f'"{k[0]} Progress Is {skills[k[0]]}"')
# print(f'"{k[1]} Progress Is {skills[k[1]]}"')
# print(f'"{k[2]} Progress Is {skills[k[2]]}"')

# # 3. إضافة المهارة الجديدة
# skills["AI"] = "20%"

# # 4. طباعة المهارة الجديدة
# print(f'"AI Progress Is {skills["AI"]}"')


# d={
#     "HTML":"90%",
#     "CSS":"80%",
#     "Python":"30%"
# }
# my_iter = iter(d)

# print(f'" {next(my_iter)} Is Progress {d["HTML"]}   "')
# print(f'" {next(my_iter)} Is Progress {d["CSS"]}   "')
# print(f'" {next(my_iter)} Is Progress {d["Python"]}   "')


# # 1. إنشاء الـ Dictionary
# skills = {
#     "HTML": "90%",
#     "CSS": "80%",
#     "Python": "30%"
# }

# # تحويل المفاتيح إلى قائمة للوصول إليها بالفهرس (Index)
# k = list(skills.keys())

# # 2. طباعة المهارات الثلاث بدون Loop
# print(f'"{k[0]} Progress Is {skills["HTML"]}"')


# # 3. إضافة المهارة الجديدة
# skills["AI"] = "20%"

# # 4. طباعة المهارة الجديدة
# print(f'"AI Progress Is {skills["AI"]}"')

# html = 80
# css = 60
# javascript = 70

# print ( html > 50 and css > 50 and javascript > 50 )


# num_one = 10
# num_two = 20
# num = 20

# print ( num > num_one or num >  num_two)
# print ( num > num_one and num > num_two)

# num_one = 10
# num_two = 20
# result = num_one + num_two
# print(result)
# result **=3
# print(result)
# result %=26000
# print(result)
# result /=5
# print(result)
# result=str(result)
# print(type(result))

# num_one = 10
# num_two = 20

# # 1. طباعة جمع المتغيرين
# print(num_one + num_two)

# # 2. طباعة نتيجة الأس 3
# print((num_one + num_two) ** 3)

# # 3. طباعة باقي القسمة على 26000
# print(((num_one + num_two) ** 3) % 26000)

# # 4. طباعة القسمة على 5
# print((((num_one + num_two) ** 3) % 26000) / 5)

# # 5. تحويل النتيجة لـ String ثم طباعة النوع type()
# print(type(str((((num_one + num_two) ** 3) % 26000) / 5)))

