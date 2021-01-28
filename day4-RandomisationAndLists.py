import random
random_integer = random.randint(1,10)
print(random_integer)
random_float = random.random()
print(random_float)
#How to create a random floating point number between 0 and 5?
#1 
random1_5_1 = random.uniform(1,5) # [1,5]
print(random1_5_1)
#2
random1_5_2 = 5*random.random()
print(random1_5_2)
#3 For a certain number of digits after decimal
N = 10
random1_5_3 = round(random.uniform(1,5),N) 
print(random1_5_3)
#better approach for 3 
random1_5_4 = "{:.10f}".format(random.uniform(1,5))
print(random1_5_4)