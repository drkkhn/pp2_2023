import re as r
s = str(input())
n = r.findall("[A-Z]+[a-z]$",s)
if n :
    print ("YES")
else :
    print ('NO')