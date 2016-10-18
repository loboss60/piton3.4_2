import csv
import random
tab_file=open('german_tab_csv.csv', 'rt',)
lol=csv.reader(tab_file,delimiter='\t')

#for row in lol:
#    print(row)
#   break




lines = []
with open('german_tab_csv.csv', 'r') as f:
    for line in f.readlines():
       line1=line.rstrip()
#       print(line1)

       line3=line1.replace( '      ','$$',100000)
       for i in range(100):
            line4 = line3.replace('  ', ' ', 100000)
            line3=line4
#       print(line3)
       line5 = line3.replace('$ ', '&', 100000)
#       print(line5)
       line6=line5.replace('$','',10000)
#       print(line6)
       words=line6.split('&')
       lines.append(words)
#    t=input("Pritisni taster da vidiš dužinu liste u list")
    print("Broj riječi je",len(lines))
#    print(lines)

#Now the funny part
counter=random.randint(0,len(lines)-1)
counter2=random.randint(0,len(lines)-1)
counter3=random.randint(0,len(lines)-1)

germ=lines[counter][0]
germ1=lines[counter2][0]
germ2=lines[counter3][0]
gerlist=[germ,germ1,germ2]
gerlist_right=[1,0,0]
ger_together=list(map(list,zip(gerlist,gerlist_right)))
#print(ger_together)
random.shuffle(ger_together)
#print(ger_together)
#print(len(ger_together))

eng=lines[counter][1]
ii=1
for words1 in ger_together:

    print(str(ii)+"."+str(words1[0]))
    ii=ii+1
gerq=input("Koja je njemačka riječ za  \n"+eng)
is1=ger_together[int(gerq)-1][1]
print(is1)
if is1==1:
    print("Tačan odgovor")
else:
    print("Pogrešan odgovor")