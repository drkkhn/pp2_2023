import re 
s = str(input())
n = re.search('^a(b*)$' , s) 
if n:
    print ("Yes") 
else :
    print ("No")