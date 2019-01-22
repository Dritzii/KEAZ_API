from classkeaz import config










def main():
    ### print(dir(config))
    data = config().get_anything('company/90/paging_bookings/2018-12-31/00:00/2019-02-04/00:00')
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

