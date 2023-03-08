import os
p=os.listdir(r'C:\Users\Gamer\Desktop\PP2 2023\lab6\dir and files\tpath')

print('It exists :', os.access(__file__, os.F_OK))
print('It is eeadable ', os.access(__file__, os.R_OK))
print('It is writable:', os.access(__file__, os.W_OK))
print('Its executable:', os.access(__file__, os.X_OK))