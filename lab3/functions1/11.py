def pal(s) :
    ss = s[::-1]
    if s==ss:
        return True
    return False
a = "abba"
print(pal(a))