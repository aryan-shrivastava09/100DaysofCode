# with open("./day25-Start/weather_data.csv", mode = "r+") as wd:
#     data = wd.readlines()

# print(data)

# import csv
# count = 0
# with open("./day25-Start/weather_data.csv") as wd:
#     data = csv.reader(wd)
#     temperatures = []
#     for row in data:
#         print(row)
#         count += 1
#         if count != 1:
#             temperatures.append(int(row[1]))
        
#     print(temperatures)
    
import pandas
data = pandas.read_csv("./day25-Start/weather_data.csv")
# print(data)
# print(data["temp"])

datadict = data.to_dict()
# print(datadict)
templist = data["temp"].to_list()
# print("Average temperature = ", round(sum(templist)/len(templist),2))
print("Average Temperature = ", round(data["temp"].mean(),2))

######
#both are same
# print(data["temp"])
# print(data.temp)
######

# maxtemp = max(templist)
maxtemp = data["temp"].max()
print(maxtemp)
print(data[data.temp == maxtemp])
monday = data[data.day == "Monday"]
print(monday.condition)
print("Monday's temperature in Farenhiet =",(float(monday.temp)*9/5 + 32))

### Create dataframe form dictionary
datadi = {
    "names": ["Aryan", "Shobhit", "Astha"],
    "score": [100,100,0]
}

datadf = pandas.DataFrame(datadi)
datadf.to_csv("./day25-Start/new_file.csv")
print(datadf)