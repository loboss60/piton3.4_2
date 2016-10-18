import os

f = open('D:\\test.txt', 'w')
for i in range(100):
    f.write(str(i)+"\n")
f.close()
try:
 os.remove('D:\\test.txt')
except OSError:
        pass