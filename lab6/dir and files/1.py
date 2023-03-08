import os  
path = os.listdir(r'C:\Users\Gamer\Desktop\PP2 2023\lab6\dir and files\tpath')
for i in path:
    if os.path.isdir(i):
        print(i)
for i in path:
    if os.path.isdir(i) or os.path.isfile(i):
        print(i)
for i in path:
    if os.path.isfile(i):
        print(i)
