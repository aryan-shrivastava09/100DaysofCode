
file1handl = open("./ex26.3/file1.txt")
list1 = []
for line in file1handl:
  line = line.strip()
  list1.append(line)

file2handl = open("./ex26.3/file2.txt")
list2=[]
for line in file2handl:
  line = line.strip()
  list2.append(line)

result = [num for num in list1 if num in list2]

###### If we don't wanna strip the files of spaces and newlines we can alternatively use

# result = [int(num) for num in list1 if num in list2]

# Write your code above 👆

print(result)