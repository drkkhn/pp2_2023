import re 
s = input()
def convert(s):
    return ''.join(x.capitalize() for x in s.split("_"))
print(convert(s))