from sys import version_info
from sys import a
py3 = version_info[0] > 2 #creates boolean value for test that Python major version > 2
print (version_info[0])
print(len(version_info))
#print(*version_info, sep='\n')
print(*version_info, sep='.')
if py3:
  response = input("Please enter your name bigger than 2: ")
else:
  response = input("Please enter your name less than 2: ")