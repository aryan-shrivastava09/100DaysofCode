# file error
# with open("./adata.txt") as file:
#   file.read()

#Key error
# dict1= {"HI":"Aryan"}
# print(dict1["hello"])

#Index error
# list1 = [1,2,3,4,5]
# print(list[5]) 

#Type Error
# text = "abc"
# print(text + 1)

#File error
# try:
#     fileh = open("./day30-Start-Exceptions/a_data.text")
#     a_dict = {"my key": "Hello"}
#     print(a_dict["your key"])
# except FileNotFoundError:
#     fileh = open("./day30-Start-Exceptions/a_data.text", mode = "w")
#     fileh.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} did not exist")
# else:
#     content = fileh.read()
#     print(content)
# finally:
#     # fileh.close()
#     # print("File was closed")
#     raise TypeError("This is an error that I made up")

try :
    weight= int(input("Enter your weight in kgs "))
except:
    print("Enter a valid number")

height = float(input("Enter your height"))
if height>3:
    raise ValueError("Human height should not exceed 3m ")

bmi = weight / (height**2)
print(bmi)

