student_score = {
    "student" : ["Aryan", "Astha", "Shobha"],
    "score" : [90,80,85]
}

## Looping through a dictionary
# for (key,value) in student_score.items():
#     print(key)

## Looping through a pandas dataframe
import pandas as pd
data = pd.DataFrame(student_score)


# for (key,value) in data.items():
#     print(value)

for (index, rows) in data.iterrows():
    print(rows.student)
    # print(rows.score)
    # print(rows)