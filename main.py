from classkeaz import config










def main():
    ### print(dir(config))
    data = config().get_anything('booking/1258871')
    print(data)










if __name__ == "__main__":
    main()










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
