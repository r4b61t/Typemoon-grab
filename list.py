from os import listdir
from os.path import isfile, join

mypath = 'C:\\Users\\chaya\\Documents\\selenium\\Type_moon\\pics'

pics = [f for f in listdir(mypath) if isfile(join(mypath, f))]

all_names = open('allnames.txt',"r")

l = []
i=0
for line in all_names:
    l.append(line.split(' ')[0])

for name in l:
    if name not in pics:
        print(name)
