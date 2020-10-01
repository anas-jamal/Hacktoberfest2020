## Base58 Checker <br>

This program checks if the user input value is base58 encoded or not.
#Logic

First it checks idiviually for 'I', 'O', 'l' and '0'
And then it checks if there are 58 unique characters
When u convert a list to a set all duplicate values will be deleted
So a string "aaa" will give:
set(string) = {'a'}
And length of the set will give u the length of the unique letters.

Requirements: python3
usage: python3 checker.py
