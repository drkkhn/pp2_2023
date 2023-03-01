import re 
s = input() 
a = re.findall("[A-Z][^A-Z]*", s)
b = " ".join(a) 
print (b)