import re 
s = input()
n = re.sub("[\s.,] , :" , s)
print(n) 