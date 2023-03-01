import re 
s = input()
x = re.findall("[A-Z][^A-Z]*" , s )
print(x) 
