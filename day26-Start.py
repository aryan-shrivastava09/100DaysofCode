numbers= [1,2,3]
# new_list = []
# for n in numbers:
#     add_1 = n+1
#     new_list.append(add_1)

# print(new_list)

#### Using list comprehension
new_list = [n+1 for n in numbers]
print(new_list)

name = "Aryan"
name_new = [l for l in name]
print(name_new)

ran = range(1,5)
new_ran = [n*2 for n in ran]
print(new_ran)

##### Conditional List comprehension
# names = ["Aryan", "Astha", "Agamya", "Siddhi"]
# new_namelist = [name for name in names if name[0]=="A"]
# print(new_namelist)

names = ["Aryan", "Eleanor", "Theodore", "Astha"]
new_namelist = [name.upper() for name in names if len(name)<=5]
print(new_namelist)
