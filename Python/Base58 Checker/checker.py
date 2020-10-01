#!bin/Python3
#This Program checks if Encoded string is base58 or not.
 
user_input = input("Enter your String: ")  #this line will take input from user 
if ('I' not in user_input) and ('O' not in user_input) and ('l' not in user_input) and (len(set(user_input)) < 58) and ('0' not in user_input):     #First it checks idiviually for 'I', 'O', 'l' and '0'And then it checks if there are 58 unique charactersWhen u convert a list to a set all duplicate values will be deletedSo a string "aaa" will give:set(string) = {'a'}And length of the set will give u the length of the unique letters
  print("The string is Base58") 
else:
  print("the string is not Base58")
