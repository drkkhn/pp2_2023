import re 
s = str(input())
n = re.search('^ab{2,3}',s)
if n :
    print ("Yes")
else :
    print("No")