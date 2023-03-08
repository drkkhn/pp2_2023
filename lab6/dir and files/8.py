import os
a=(r"C:\Users\Gamer\Desktop\PP2 2023\lab6\dir and files\tpath\aue.txt")
if os.path.exists(a):
    os.remove(a)
else:
    print("There is no such file.")