import re as r 
s = str(input())
n = r.findall("a.*?b$",s)
if n :
    print('yes')
else:
    print('no')