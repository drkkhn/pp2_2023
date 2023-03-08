s = input() 
def counter(s):
    cnt = 0  
    for i in s :
        if ((ord(i)) >= 65 and (ord(i))<=90) or ((ord(i))>=97 and (ord(i))<=122):
            cnt += 1 
    return cnt 
print(counter(s)) 