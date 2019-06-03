"""
Author: John Pham
intent: Geocode lng/lats into addresses

"""

import requests


class config():
    def __init__(self):
        self.base_url = "https://api.opencagedata.com/geocode/v1/json?q="
        self.key = "7ef52ab4364c49feb4cb9cfca882c2f5"
        print(self.base_url)

    def reverse_api(self, lat, lng):
        url = self.base_url + lat + "%2C%20" + lng + "&key=" + self.key
        print(url)
        try:
            r = requests.get(url)
            print(r)
            print(r.content)
            if r.status_code == [200, '200']:
                print(r.status_code + " Successful request")
                return(r.json())
            elif r.status_code == [404, '404', 401, '401']:
                print(r.status_code + " unsuccessful request")
                return(False)
            else:
                print(r.status_code)
                return(False)
        except:
            print("failed to get request")
            return(False)

    def forward_api(self, address):
        url = self.base_url + str(address) + "+&key=" + str(self.key)
        print(url)
        try:
            r = requests.get(url)
            print(r)
            print(r.content)
            if r.status_code == [200, '200']:
                print(r.status_code + " Successful request")
                return(r.json())
            elif r.status_code == [404, '404', 401, '401']:
                print(r.status_code + " unsuccessful request")
                return(False)
            else:
                print(r.status_code)
                return(False)
        except:
            print("failed to get request")
            return(False)


def main():
    def importcsv():
        import csv
        file = open("C:/Users/John Pham/Desktop/csv.csv")### enter pathway to csv here
        reader = csv.reader(file)
        reader.__next__()
        for each in reader:
            yield each
        for each in importcsv():
            print(each)

    for each in importcsv():
        lat = each[0]
        lng = each[1]
        data = config()
        r = data.reverse_api(lat , lng)
        print(r)




if __name__ == "__main__":
    main()