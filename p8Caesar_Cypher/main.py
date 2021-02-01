##########
##########
##########

####### Only encypt
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt (text, shift):
#   word = []
#   eword = ""
#   for i in range(0, len(text)):
#     #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
#     #e.g. 
#     #plain_text = "hello"
#     #shift = 5
#     #cipher_text = "mjqqt"
#     #print output: "The encoded text is mjqqt"
#     pos1 = alphabet.index(text[i])
#     if (pos1+shift) < 26 :
#       letter = alphabet[pos1+shift]
#       word.append(letter)
#     else :
#       letter = alphabet[pos1 + shift - 26]
#       word.append(letter)
#     ##HINT: How do you get the index of an item in a list:
#     #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
#   for w in word:
#     eword += w

#   print(f"The encoded text is {eword} ")
#     ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
# if direction == "encode":
#   encrypt(text, shift)

##########
##########
##########

####### With Decrypt and looping of control
# flag = "yes"
# while flag == "yes":
#   alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#   text = input("Type your message:\n").lower()
#   shift = int(input("Type the shift number:\n"))

#   #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#   def encrypt (text, shift):
#     word = []
#     eword = ""
#     for i in range(0, len(text)):
#       #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
#       #e.g. 
#       #plain_text = "hello"
#       #shift = 5
#       #cipher_text = "mjqqt"
#       #print output: "The encoded text is mjqqt"
#         if text[i] not in alphabet:
#           letter = text[i]
#           word.append(letter)
#         else:
#           pos1 = alphabet.index(text[i])
#           if (pos1+shift) < 26 :
#             letter = alphabet[pos1+shift]
#             word.append(letter)
#           else :
#             letter = alphabet[pos1 + shift - 26]
#             word.append(letter)
#       ##HINT: How do you get the index of an item in a list:
#       #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
#     for w in word:
#       eword += w

#     print(f"The encoded text is {eword} ")
#       ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#   #TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
#   def decrypt(text, shift):
#     word = []
#     eword =""
#     for i in range(0,len(text)):
#       if text[i] not in alphabet:
#         letter = text[i]
#         word.append(letter)
#       else:
#         pos2 = alphabet.index(text[i])
#         if pos2 - shift >= 0:
#           letter = alphabet[pos2-shift]
#           word.append(letter)
#         else:
#           letter = alphabet[pos2 - shift + 26]
#           word.append(letter)
#     for w in word:
#       eword += w
#     print(f"The decoded text is {eword}")
#     #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
#     #e.g. 
#     #cipher_text = "mjqqt"
#     #shift = 5
#     #plain_text = "hello"
#     #print output: "The decoded text is hello"


#   #TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

#   #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
#   if text == "end":
#     print("Thank You")
#   if direction == "encode":
#     encrypt(text,shift)
#   elif direction == "decode":
#     decrypt(text,shift)
#   flag = input("Type 'yes' if you want to go again. Otherwise type 'no'\n.")

##########
##########
##########

### Single Function

import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
flag= "yes"
while flag == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if shift > 25:
    shift = shift % 25
  def caesar(start_text, shift, direction):
    word = []
    eword = ""
    if direction == "encode":
      s = shift
      l = -26
    if direction == "decode":
      s = -shift
      l = 26
    for i in range(0,len(text)):
      if text[i] not in alphabet:
        letter = text[i]
        word.append(letter)
        
      else:
        pos = alphabet.index(text[i])
        if pos - s >= 0 and pos + s <26:
          letter = alphabet[pos+s]
          word.append(letter)
          
        else:
          letter = alphabet[pos + s + l]
          word.append(letter)
          
    for w in word:
      eword += w
    print(f"The {direction}d text is {eword}")
  caesar(text,shift,direction)  
  flag = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")