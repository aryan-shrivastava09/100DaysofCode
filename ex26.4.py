sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
listwords = sentence.split(" ")
# for i in range(0, len(sentence)):
#   if sentence[i] != " " and i != len(sentence)-1:
#     w += sentence[i]
#   else:
#     if i == len(sentence) - 1:
#       w += sentence[len(sentence) -1] 
#     listwords.append(w)
#     w= ""


result = {word : len(word) for word in listwords}


print(result)