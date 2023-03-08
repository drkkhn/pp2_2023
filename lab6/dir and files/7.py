file1=open(r"C:\Users\Gamer\Desktop\PP2 2023\lab6\dir and files\tpath\1.txt", "r")
file2=open(r"C:\Users\Gamer\Desktop\PP2 2023\lab6\dir and files\tpath\2.txt", "w")
for line in file1:
    file2.write(line)