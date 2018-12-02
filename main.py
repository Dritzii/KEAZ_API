from classkeaz import config


print(dir(config))

credentials = config("transdev-melbourne.keaz.software")
data = credentials.get_anything('vehicle/kits')
print(data)

for key in data:
    print(key, sep = ",")




















"""
used to grab booking details

for i,o in data.items():
    a = str(i)
    b = str(o)
    print(a + " : " +  b)
import csv
with open("output.csv",'w') as file:
    writer = csv.writer(file,delimiter=',')
    for i,o in data.items():
        writer.writerow([i,o])
        file.close

"""

