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

# age = 17
# print("App Is Suitable For You" if age > 6 else "App Is Not Suitable For You")
# # Needed Output

# "App Is Suitable For You" # If Age Larger Than 6
# "App Is Not Suitable For You" # if Age Smaller Than 16
# Input Example One "Egypt"
# Input Example Two "Ghana"

# country = input("Input Your Country ")
# countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
# price = 100
# discount = 30
# if country in countries:
#     print(f"Your Country Eligible For Discount And The Price After Discount Is ${price - discount}")
# else:
#     print(f"Your Country Not Eligible For Discount And The Price Is ${price}")
# # Needed Output
# "Your Country Eligible For Discount And The Price After Discount Is $70" # Egypt Example
# "Your Country Not Eligible For Discount And The Price Is $100" # Ghana Example

# num = int(input("Input Your Number "))
# if num <= 0:
#     print("Number Is Wrong")
# elif num > 0:
#     while num > 1:
#         num -= 1
#         if num  == 6:
#             continue
#         print(num)
#     print("Done")

# Input
# friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
# ignored_count = 0
# while friends:
#         friend = friends.pop(0)
#         if friend[0].islower():
#             ignored_count += 1
#             continue
#         print(friend)
# print(f"Done, Ignored {ignored_count} Names")


# Code
# skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

# while skills:
#     print('"' + skills.pop(0) + '"')


# my_friends = []
# max_friends = 4

# while len(my_friends) < max_friends:
#     name = input("Add friend name: ").strip()
    
#     if name.isupper():
#         print("Invalid Name")
#     elif name.islower():
#         name = name.capitalize()
#         my_friends.append(name)
#         print(f"Friend {name} Added => 1st Letter Become Capital")
#         print(f"Names Left in List Is {max_friends - len(my_friends)}")
#     else:
#         my_friends.append(name)
#         print(f"Friend {name} Added")
#         print(f"Names Left in List Is {max_friends - len(my_friends)}")

# print(my_friends)

# for number in range(1, 21):
#     if number == 6:
#         continue
#     print(number)
# mySkills = {
#   "Html": "90%",
#   "Css": "60%",
#   "PHP": "70%",
#   "JS": "80%",
#   "Python": "90%",
#   "MySQL": "60%"
# }

# for skill in mySkills:
#     print(f"{skill} => {mySkills[skill]}")

# peoples = {
#   "Osama": {
#     "Html": "70%",
#     "Css": "80%",
#     "Js": "70%"
#   },
#   "Ahmed": {
#     "Html": "90%",
#     "Css": "80%",
#     "Js": "90%"
#   },
#   "Sayed": {
#     "Html": "70%",
#     "Css": "60%",
#     "Js": "90%"
#   }
# }

# for name in peoples:

#   print(f"Skills and Progress For {name} Is: ")

#   for skill in peoples[name]:

#     print(f"{skill.upper()} => {peoples[name][skill]}")


# mySkills = {
#   "HTML": "80%",
#   "CSS": "90%",
#   "JS": "70%",
#   "PHP": "80%"
# }

# print(mySkills.items())

# myUltimateSkills = {
#   "HTML": {
#     "Main": "80%",
#     "Pugjs": "80%"
#   },
#   "CSS": {
#     "Main": "90%",
#     "Sass": "70%"
#   }
# }

# for main_key , maim_value in myUltimateSkills.items():
#     print(f"{main_key}:")
#     for ch_key , ch_value in maim_value.items():
#         print(f"{ch_key} => {ch_value}")
  

# my_nums = [15, 81, 5, 17, 20, 21, 13]
# count = 1
# for num in my_nums:
#     if num % 5 == 0:
#         print(f" {count} {num} ")
#     count += 1
# print("Done")
# Input

# my_nums = [15, 81, 5, 17, 20, 21, 13]
# for i, num in enumerate(my_nums):
#     if num % 5 == 0:
#         print(f"{i} => {num}")

# print("All Numbers Printed")
# l=range(1, 21)
# for i in l:
#     if i in [6,8,12]:
#         continue
#     print(f"{str(i).zfill(2)}")


# my_ranks = {
#   'Math': 'A',
#   "Science": 'B',
#   'Drawing': 'A',
#   'Sports': 'C'
# }
# total = 0
# for m_key,m_value in my_ranks.items():
#     if m_value == 'A':
#         rank = 100
#     elif m_value == 'B':
#         rank = 80
#     elif m_value == 'C':
#         rank = 40
#     total+=rank
#     print(f"My Rank in {m_key} Is {m_value} And This Equal {rank} Points")
# print(f"Total Points Is {total}")


# students = {
#   "Ahmed": {
#     "Math": "A",
#     "Science": "D",
#     "Draw": "B",
#     "Sports": "C",
#     "Thinking": "A"
#   },
#   "Sayed": {
#     "Math": "B",
#     "Science": "B",
#     "Draw": "B",
#     "Sports": "D",
#     "Thinking": "A"
#   },
#   "Mahmoud": {
#     "Math": "D",
#     "Science": "A",
#     "Draw": "A",
#     "Sports": "B",
#     "Thinking": "B"
#   }
# }

# for s_key,s_value in students.items():
#     total = 0
#     print(f"-"*50)
#     print(f"Student Name Is {s_key}")
#     print(f"-"*50)
#     for m_key,m_value in s_value.items():
#         if m_value == 'A':
#             rank = 100
#         elif m_value == 'B':
#             rank = 80
#         elif m_value == 'C':
#             rank = 40
#         elif m_value == 'D':
#             rank = 20
#         total+=rank
#         print(f"- {m_key} => {m_value} => {rank} Points")
#     print(f"Total Points For {s_key} Is {total}")
    


# def calc(*numbers):
#     total = 0
#     for number in numbers:
#         if number == 10:
#             continue
#         elif number == 5:
#             total -= number
#         else:
#              total += number
#     return total
# print(calc(10, 20, 30, 10, 15))
# print(calc(10, 20, 30, 10, 15, 5, 100))



# def show_skills(name, *skills):
#     if not skills:
#         print(f"Hello {name} You Have No Skills")
#     else:
#         print(f"Hello {name} Your Skills Is:")
#         for skill in skills:
#             print(f"- {skill}")

# show_skills("Osama")
# print("-"*50)
# show_skills("Ahmed", "HTML", "CSS", "JS")





# def say_hello(name="Unknown", age="Unknown", country="Unknown"):
#     return f"Hello {name}, your age is {age}, and you live in {country}"
# print(say_hello("Osama", 38, "Egypt"))
# print(say_hello())


# def calculate(num_one, num_two, operation="add"):
#     if operation == "A" or operation == "AdD" or operation == "a":
#         return num_one + num_two
#     elif operation == "S" or operation == "subTRACT" or operation == "s":
#         return num_one - num_two
#     elif operation == "Multiply" or operation == "*" or operation == "m":
#         return num_one * num_two
#     elif operation == "divide" or operation == "/" or operation == "d":
#         return num_one / num_two
#     else:
#         return "Invalid Operation"

# print(calculate(10, 20)) # 30
# print(calculate(10, 20, "AdD")) # 30
# print(calculate(10, 20, "a")) # 30
# print(calculate(10, 20, "A")) # 30

# print(calculate(10, 20, "S")) # -10
# print(calculate(10, 20, "subTRACT")) # -10

# print(calculate(10, 20, "Multiply")) # 200
# print(calculate(10, 20, "m")) # 200
# print(calculate(10, 20, "ff")) # 200


# hello = lambda name, age, country: f"Hello {name}, your age is {age}, and you live in {country}"

# print(hello(input("Enter Your Name: "), input("Enter Your Age: "), input("Enter Your Country: ")))

# def mySkills(**skills):
#     if not skills:
#         return "You Have No Skills"
#     else:
#         for k_skill,v_skill in skills.items():
#             print(f"My Skill Is {k_skill} And My Progress Is {v_skill}")
# print("-"*50)
# print(mySkills(HTML="80%", CSS="90%", JS="70%", PHP="80%", Python="90%", MySQL="60%"))
# print(mySkills())


# ------------------------
# -- Function Recursion --
# ------------------------
# ---------------------------------------------------------------------
# -- To Understand Recursion, You Need to First Understand Recursion --
# ---------------------------------------------------------------------

# Test Word [ WWWoooorrrldd ] # print(x[1:])

def cleanWord(word):

  if len(word) == 1:

    return word

  print(f"Print Start Function {word}")

  if word[0] == word[1]:

    print(f"Print Before Condition {word}")

    return cleanWord(word[1:])

  print(f"Print Before Return {word}")
  return word[0] + cleanWord(word[1:])

  # Stash [ World ]

print(cleanWord("WWWoooorrrldd"))