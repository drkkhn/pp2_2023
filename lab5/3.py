import re 
s = str(input())
x = re.findall("[a-z]",s)
if x : 
    print("Yes")
else :
    print("No")