import re 
s = input()
def convert(s):
    ans = [s[0]]
    for i in s[1:] :
        if i in ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            ans.append("_")
            ans.append(i)
        else :
            ans.append(i)
    return ''.join(ans)
print(convert(s))
