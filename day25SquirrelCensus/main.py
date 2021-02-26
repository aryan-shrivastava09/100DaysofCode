import pandas as pd
data = pd.read_csv("./day25SquirrelCensus/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gs = len(data[data["Primary Fur Color"]=="Gray"])
bs = len(data[data["Primary Fur Color"]=="Black"])
cs = len(data[data["Primary Fur Color"]=="Cinnamon"])


newdatadic = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gs,bs,cs]
}

newdataf = pd.DataFrame(newdatadic)
newdataf.to_csv("./day25SquirrelCensus/newdata.csv")


