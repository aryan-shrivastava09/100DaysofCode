#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

nameshandl = open("./p24Mail_Merging/Input/Names/invited_names.txt", mode = "r+")
letter =  open("./p24Mail_Merging/Input/Letters/starting_letter.txt", mode= "r+")
sl = letter.read()

namelist = []

for line in nameshandl:
    name = line.strip()
    namelist.append(name)

for i in range(0,len(namelist)):
    sl.replace("[name]", namelist[i])
    f = open(f"./p24Mail_Merging/Output/ReadyToSend/{namelist[i]}.txt", mode= "w+")
    f.write(sl.replace("[name]", namelist[i]))

nameshandl.close()
letter.close()





