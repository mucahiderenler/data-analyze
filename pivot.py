import sys
import csv

infos = []
name = ""

f = open('player_career.csv','r')
try:
    datos = None
    reader = csv.DictReader(f)
    for row in reader:
        datos = []
        datos.append(row[('firstname')])
        datos.append(row[('minutes')])
        datos.append(row[('pts')])
        datos.append(row[('reb')])
        datos.append(row[('asts')])
        datos.append(row[('stl')])
        datos.append(row[('blk')])
        infos.append(datos)

finally:
    f.close()

f = open('pivot_player.csv','w')
try:
    fieldNames = ['name','minutes','points','reb','asts','stl','blk']
    writer = csv.writer(f)
    writer.writerow(fieldNames)
    for i in range(1,len(infos)):
        writer.writerow(infos[i])
    writer.writerow(infos[0])
finally:
    f.close()

#for i in range(1,len(infos)):
 ###     print(infos[i])
#print(infos[1])




