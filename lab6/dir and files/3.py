import os
p=(r'C:\Users\Gamer\Desktop\PP2 2023\lab6\dir and files\tpath')

if os.path.exists(p):
    print("filename and directory portion of the given path")
    print(os.path.basename(p))
    print(os.path.dirname(p))
else:
    print("Doesnt exist")