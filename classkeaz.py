"""
write a class based on KEAZ API for use
Author: John Pham

"""

import requests


class config:
    def __init__(self, host=None):  # constructor
        self.api_base = 'http://api.keaz.software/v1/'
        if host is None:
            self.host = 'keaz.keaz.software'
        else:
            self.host = host
        if not self.login():    ### references login(self)
            raise Exception
        self.headers = {'X-Source-Host': self.host,
                        'token': self.token}

    def login(self):
        print('Logging in')
        headers = {'X-Source-Host': self.host,
                   'app_name': 'Johns Script',
                   'version': '1.40.0',
                   'device_type': 'SCRIPT'}
        pw = input("Enter your password for Keaz API: ")
        form = {'email': 'john@keaz.co',
                'password': pw}
        url = self.api_base + 'login'
        print(headers)
        print(url)
        try:
            res = requests.post(url, headers=headers, json=form)
            if res.status_code not in [200, '200']:
                print('Failed to Login Status Code : {}'.format(
                    str(res.status_code)))
                return False
            else:
                self.token = res.json()['token']
                print('Successful Log In')
                return True
        except:
            print('Failed to generate Login Request')
### getters 
    def getanything(self): 
        a = input("getting anything you ask for after/   <-  ")
        url = self.api_base + a
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code in [200, '200']:
                print("request successful")
                return(r.json())
            elif r.status_code in [401, '401']:
                print("Something is wrong with that request status code {}".format(
                    str(r.status_code)))
                return False
            else:
                print("try again")
        except:
            print("no can do man")

    def getbookings(self):
        a = input("Enter the booking number: ")
        url = self.api_base + 'booking/' + a
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code in [200, '200']:
                print("request successful")
                return(r.json())
            elif r.status_code in [401, '401']:
                print("Something is wrong status code {}".format(
                    str(r.status_code)))
                return False
            else:
                print("no can do")
        except:
            print("sorry status code {}".format(str(r.status_code)))

    def get_branches(self):
        url = self.api_base + 'branches'
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code in [200, '200']:
                print("great success status code {}".format(str(r.status_code)))
                return(r.json())
            elif r.status_code in [401, '401']:
                print("Error {}".format(str(r.status_code)))
                return False
            else:
                print("no no no {}".format(str(r.status_code)))
        except:
            print("No can Do")

    def get_users(self):
        url = self.api_base + 'users'
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code in [200, '200']:
                print("Great success, status code {}".format(str(r.status_code)))
                return(r.json())
            elif r.status_code in [401, '401']:
                print("Error {}".format(str(r.status_code)))
                return False
            else:
                print("Something is wrong {}".format(str(r.status_code)))
        except:
            print("next time")

    def get_vehicles(self):
        url = self.api_base + 'vehicles'
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code in [200, '200']:
                print("Great success, status code {}".format(str(r.status_code)))
                return(r.json())
            elif r.status_code in [401, '401']:
                print("Error {}".format(str(r.status_code)))
                return False
            else:
                print("Something is wrong {}".format(str(r.status_code)))
        except:
            print("next time")

    def get_costcentres(self):
        url = self.api_base + 'cost-centres'
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code in [200, '200']:
                print("Great success, status code {}".format(str(r.status_code)))
                return(r.json())
            elif r.status_code in [401, '401']:
                print("Error {}".format(str(r.status_code)))
                return False
            else:
                print("Something is wrong {}".format(str(r.status_code)))
        except:
            print("next time")

    def get_companies(self):
        url = self.api_base + 'companies'
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code in [200, '200']:
                print("Great SUccess, status code {}".format(str(r.status_code)))
                return(r.json())
            elif r.status_code in [400, '400']:
                print("Error {}".format(str(r.status_code)))
                return False
            else:
                print("status code {}".format(str(r.status_code)))
        except:
            print("error")
# modifying a user ## mutators

    def create_user(self, name, email, idnumb, contactnumber,
                 licensenumber, licenseexpmonth, licenseexpiryyear,
                 licensetype, liensecountry, ccid, activatedviacompanyid):
        a = input("Please tell me who you want to modify:  ")
        temp = self.api_base + 'user/' + str(a)
        body = {
                "name": name,
                "email": email,
                "employee_id": idnumb,
                "contact_number": contactnumber,
                "license_number": licensenumber,
                "license_expiry_month": licenseexpmonth,
                "license_expiry_year": licenseexpiryyear,
                "license_type": licensetype,
                "license_country": liensecountry,
                "cost-centre_id": ccid,
                "activated-via-company-id": activatedviacompanyid
        }
        try:
            res = requests.post(temp, json=body, headers=self.headers)
            if res.status_code in [401, '401']:
                print('failed to access the resource to update')
                return False
            elif res.status_code in [200, '200']:
                print('awesome, i have found it')
                return(res.json())
            else:
                print('Something is wrong, please check the script')
        except:
            print('Status code {}'.format(str(res.status_code)))
# creating a booking

    def create_booking(self, date, branch, user_id, vehicle, cost_centre, trip_purpose):
        temp_url = self.api_base + 'booking'
        payload = {
                "node_id": "",
                "node_sel": "",
                "drop_off_node_id": "",
                "drop_off_node_sel": "",
                "user_id": user_id,
                "sub_user_id": "",
                "cost-centre_id": cost_centre,
                "trip_type": "Business",
                "trip_purpose": 'trip_purpose',
                "trip_purpose_text": "",
                "branch_id": branch,
                "recurring_enable": "False",
                "enable_sub_user": "False",
                "trip_types": [
                    "Business",
                    "Private"
                ],
                "start_timezone_offset": -36000,
                "end_timezone_offset": -36000,
                "drop_off_branch_id": branch,
                "start_time": '09:00',   # todo get value
                "start_date":  str(date),  # todo get value
                "end_date": str(date),
                "end_time": '17:00',
                "vehicle_id": vehicle
        }
        print(temp_url)
        print(payload)
        try:
            post = requests.post(
                temp_url, data=payload, headers=self.headers)
            if post.status_code in [201, '201', 200, '200']:
                print('Completed your update')
                return post.status_code
            elif post.status_code in [401, '401', 400, '400']:
                print('failed to initialize')
                return False
        except:
            print('failed to update: ' + ' ' + str(post.status_code))

# create to vehicles

    def create_vehicle(self):
        a = input("enter the enpoint for your vehicle: ")
        url = self.api_base + "vehicle/" + str(a)
        body = {
                "registration": '',
                "year": '',
                "transmission": '',
                "seat_number": '',
                "fuel_type": '',
                "name": '',
                "asset_no": '',
                "key_no": '',
                "body_colour": '',
                "license_type": '',
                "kms_start": '',
                "kms_current": '',
                "availability_weekend": '',
                "availability_afterhours": '',
                "comments": '',
                "vehicle_cost": '',
                "vehicle_cost_type": ''
        }
        try:
            res = requests.put(url, headers=self.headers, json=body)
            if res.status_code in [200, '200', 201, '201']:
                print("success")
            elif res.status_code in [401, '401', '400', 400]:
                print("not successful")
            else:
                print("failed to update data")
        except:
            print("Failed")
# creating a new branch

    def create_branch(self, name, slug, address, lat, long, geohash, avabilityafterhours, avabilityweekends, businessstart, businessend):
        url = self.api_base + 'branch'
        body = {
                'name': name,
                'slug': slug,
                'address': address,
                'lat': lat,
                'long': long,
                'geohash': geohash,
                'avaibility_afterhours': avabilityafterhours,
                'avaibility_weekends': avabilityweekends,
                'business_hours_start': businessstart,
                'business_hours_end': businessend
        }
        try:
            res = requests.post(url, headers=self.headers, json=body)
            if res.status_code in [201, '201']:
                print("Success")
                return(res.json())
            elif res.status_code in [401, '401']:
                print("Error {}".format(str(res.status_code)))
                return False
            else:
                print("status code: {}".format(str(res.status_code)))
        except:
            print("check script")
## create cost centre
    def create_cc(self,name,code):
        url = self.api_base + 'cost-centre'
        body = {
            'name':name,
            'code':code
        }
        try:
            res = requests.post(url, headers= self.headers, json=body)
            if res.status_code in [201, '201']:
                print("Success")
                return(res.json())
            elif res.status_code in [401, '401']:
                print("Error {}".format(str(res.status_code)))
                return False
            else:
                print("status code: {}".format(str(res.status_code)))
        except:
            print("check script")

# single update to key, values for vehicles
    def update_vehicle(self, reg,year,trans,seat,fueltype,name,assetno,keyno,bodycolor,licensetype,kmstart,kmcurrent,availweekend,availafter,comments,vehiclecost,costtype):
        a = input("enter the enpoint for your vehicle: ")
        url = self.api_base + "vehicle/" + a
        body = {
                "registration": reg,
                "year": year,
                "transmission": trans,
                "seat_number": seat,
                "fuel_type": fueltype,
                "name": name,
                "asset_no": assetno,
                "key_no": keyno,
                "body_colour": bodycolor,
                "license_type": licensetype,
                "kms_start": kmstart,
                "kms_current": kmcurrent,
                "availability_weekend": availweekend,
                "availability_afterhours": availafter,
                "comments": comments,
                "vehicle_cost": vehiclecost,
                "vehicle_cost_type": costtype
        }
        try:
            res = requests.put(url, headers=self.headers, json=body)
            if res.status_code in [200, '200', 201, '201']:
                print("success")
                return res.json()
            elif res.status_code in [401, '401', '400', 400]:
                print("not successful")
                return False
            else:
                print("failed to update data")
        except:
            print("Failed")
# update cost centre            
    def update_cc(self,name,code):
        url = self.api_base + 'cost-centre'
        body = {
            'name':name,
            'code':code
        }
        try:
            res = requests.put(url, headers= self.headers, json=body)
            if res.status_code in [201, '201']:
                print("Success")
                return(res.json())
            elif res.status_code in [401, '401']:
                print("Error {}".format(str(res.status_code)))
                return False
            else:
                print("status code: {}".format(str(res.status_code)))
        except:
            print("check script")
### update branch               
    def update_branch(self, name, slug, address, lat, long, geohash, avabilityafterhours, avabilityweekends, businessstart, businessend):
        url = self.api_base + 'branch'
        body = {
                'name': name,
                'slug': slug,
                'address': address,
                'lat': lat,
                'long': long,
                'geohash': geohash,
                'avaibility_afterhours': avabilityafterhours,
                'avaibility_weekends': avabilityweekends,
                'business_hours_start': businessstart,
                'business_hours_end': businessend
        }
        try:
            res = requests.put(url, headers=self.headers, json=body)
            if res.status_code in [201, '201']:
                print("Success")
                return(res.json())
            elif res.status_code in [401, '401']:
                print("Error {}".format(str(res.status_code)))
                return False
            else:
                print("status code: {}".format(str(res.status_code)))
        except:
            print("check script") 
## update user                     
    def update_user(self, name, email, idnumb, contactnumber,
                 licensenumber, licenseexpmonth, licenseexpiryyear,
                 licensetype, liensecountry, ccid, activatedviacompanyid):
        a = input("Please tell me who you want to modify:  ")
        temp = self.api_base + 'user/' + str(a)
        body = {
                "name": name,
                "email": email,
                "employee_id": idnumb,
                "contact_number": contactnumber,
                "license_number": licensenumber,
                "license_expiry_month": licenseexpmonth,
                "license_expiry_year": licenseexpiryyear,
                "license_type": licensetype,
                "license_country": liensecountry,
                "cost-centre_id": ccid,
                "activated-via-company-id": activatedviacompanyid
        }
        try:
            res = requests.put(temp, json=body, headers=self.headers)
            if res.status_code in [401, '401']:
                print('failed to access the resource to update')
                return False
            elif res.status_code in [200, '200']:
                print('awesome, i have found it')
                return(res.json())
            else:
                print('Something is wrong, please check the script')
        except:
            print('Status code {}'.format(str(res.status_code)))
    def __str__(self):
        pass


def main():
    config()


if __name__ == "__main__":
    main()
