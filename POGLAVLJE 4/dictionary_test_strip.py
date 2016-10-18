import csv
tab_file=open('german_tab_csv.csv', 'rt',)
lol=csv.reader(tab_file,delimiter='\t')





line="  xxx yyyy"
print(len(line))
line1=line.strip()
line2=line.rstrip('\t')
line3=line.rstrip(' ')
print(len(line))
 #       print(line.strip().split(r'\s{2,}'))



lista=['jedan','dva','tri','cetiri']
print(len(lista))