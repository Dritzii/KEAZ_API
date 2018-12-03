'''
write a class based on KEAZ API for use
Author: John Pham
'''
import requests


class config(object):
    def __init__(self, host=None):  # constructor
        self.api_base = '://../v1/'
        if host is None:
            self.host = '..'
        else:
            self.host = host
        if not self.login():  # references login(self)
            raise Exception
        self.headers = {'--': .,
                        '': .}
        print(host)
        print(self.headers)

    def login(self):
        print('Logging in')
        headers = {'X-Source-Host': self.host,
                   'app_name': 'Johns Script',
                   'version': '1.40.0',
                   'device_type': 'SCRIPT'}
        #pw = input('Enter your password for Keaz API: ')
        form = {'email': ',
                'password':   # pw}
        url = self.api_base + 'login'
        print(headers)
        print(url)
        try:
            r = requests.post(url, headers=headers, json=form)
            if r.status_code not in [200, '200']:
                print('Failed to Login Status Code : {}'.format(
                    str(r.status_code)))
                return False
            else:
                self.token = r.json()['token']
                print('Successful Log In status code: {}'.format(
                    str(r.status_code)))
                print(r.headers)
                return r.json()
        except:
            print('Failed to generate Login Request')

    def get_anything(self, a):  # getters
        url = self.api_base + str(a)
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code in [200, '200']:
                print('request successful')
                return(r.json())
            elif r.status_code in [401, '401']:
                print('Something is wrong with that request status code {}'.format(
                    str(r.status_code)))
                return False
            else:
                print('try again')
        except:
            print('no can do man')

    def get_companies(self):
        url = self.api_base + 'companies'
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code in [200, '200']:
                print('You have successfully logged in {}'.format(
                    str(r.status_code)))
                return(r.json())
            elif r.status_code in [400, '400']:
                print('Error status code {}'.format(str(r.status_code)))
                return False
            else:
                print('A different error {}'.format(str(r.status_code)))
        except:
            print('Error')

    def get_bookings(self):
        a = input('Enter the booking number: ')
        url = self.api_base + 'booking/' + a
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code in [200, '200']:
                print('request successful')
                return(r.json())
            elif r.status_code in [401, '401']:
                print('Something is wrong status code {}'.format(
                    str(r.status_code)))
                return False
            else:
                print('no can do')
        except:
            print('sorry status code {}'.format(str(r.status_code)))

    def get_all_branches(self):
        url = self.api_base + 'branches'
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code in [200, '200']:
                print('great success status code {}'.format(str(r.status_code)))
                return(r.json())
            elif r.status_code in [401, '401']:
                print('Error {}'.format(str(r.status_code)))
                return False
            else:
                print('no no no {}'.format(str(r.status_code)))
        except:
            print('No can Do')

    def get_all_users(self):
        url = self.api_base + 'users'
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code in [200, '200']:
                print('Great success, status code {}'.format(str(r.status_code)))
                return(r.json())
            elif r.status_code in [401, '401']:
                print('Error {}'.format(str(r.status_code)))
                return False
            else:
                print('Something is wrong {}'.format(str(r.status_code)))
        except:
            print('next time')

    def get_all_vehicles(self):
        url = self.api_base + 'vehicles'
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code in [200, '200']:
                print('Great success, status code {}'.format(str(r.status_code)))
                return(r.json())
            elif r.status_code in [401, '401']:
                print('Error {}'.format(str(r.status_code)))
                return False
            else:
                print('Something is wrong {}'.format(str(r.status_code)))
        except:
            print('next time')

    def get_all_costcentr(self):
        url = self.api_base + 'cost-centr'
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code in [200, '200']:
                print('Great success, status code {}'.format(str(r.status_code)))
                return(r.json())
            elif r.status_code in [401, '401']:
                print('Error {}'.format(str(r.status_code)))
                return False
            else:
                print('Something is wrong {}'.format(str(r.status_code)))
        except:
            print('next time')

    def get_all_companies(self):
        url = self.api_base + 'companies'
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code in [200, '200']:
                print('Great Success, status code {}'.format(str(r.status_code)))
                return(r.json())
            elif r.status_code in [400, '400']:
                print('Error {}'.format(str(r.status_code)))
                return False
            else:
                print('status code {}'.format(str(r.status_code)))
        except:
            print('error')

    def get_all_kits(self):
        url = self.api_base + 'vehicle/kits'
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code in [200, '200']:
                print('Great Success, status code {}'.format(str(r.status_code)))
                return r.json()
            elif r.status_code in [400, '400']:
                print('Error: {}'.format(str(r.status_code)))
                return False
            else:
                print('error {}'.format(str(r.status_code)))
        except:
            print('Error status code: {}'.format(str(r.status_code)))

    def create_user(self, name, email, idnumb, contactnumber,
                    licensenumber, licenseexpmonth, licenseexpiryyear,
                    licensetype, liensecountry, ccid, activatedviacompanyid):
        a = input('Please tell me who you want to modify:  ')
        url = self.api_base + 'user/' + str(a)
        body = {
            'name': name,
            'email': email,
            'employee_id': idnumb,
            'contact_number': contactnumber,
            'license_number': licensenumber,
            'license_expiry_month': licenseexpmonth,
            'license_expiry_year': licenseexpiryyear,
            'license_type': licensetype,
            'license_country': liensecountry,
            'cost-centre_id': ccid,
            'activated-via-company-id': activatedviacompanyid
        }
        try:
            r = requests.post(url, json=body, headers=self.headers)
            if r.status_code in [401, '401']:
                print('failed to access the rource to update')
                return False
            elif r.status_code in [200, '200']:
                print('awesome, i have found it')
                return(r.json())
            else:
                print('Something is wrong, please check the script')
        except:
            print('Status code {}'.format(str(r.status_code)))

    def create_booking(self, date, branch, user_id, vehicle, cost_centre, trip_purpose, starttime, startdate, enddate, endtime):
        temp_url = self.api_base + 'booking'
        payload = {
            'node_id': '',
            'node_sel': '',
            'drop_off_node_id': '',
            'drop_off_node_sel': '',
            'user_id': user_id,
            'sub_user_id': '',
            'cost-centre_id': cost_centre,
            'trip_type': 'Business',
            'trip_purpose': trip_purpose,
            'trip_purpose_text': '',
            'branch_id': branch,
            'recurring_enable': 'False',
            'enable_sub_user': 'False',
            'trip_types': [
                'Business',
                'Private'
            ],
            'start_timezone_offset': -36000,
            'end_timezone_offset': -36000,
            'drop_off_branch_id': branch,
            'start_time': starttime,   # todo get value
            'start_date':  startdate,  # todo get value
            'end_date': enddate,
            'end_time': endtime,
            'vehicle_id': vehicle
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

    def create_vehicle(self, reg, year, trans, seat, fueltype, name, assetno, keyno, bodycolor, licensetype, kmstart, kmcurrent, availweekend, availafter, comments, vehiclecost, costtype):
        a = input('enter the enpoint for your vehicle: ')
        url = self.api_base + 'vehicle/' + a
        body = {
            'registration': reg,
            'year': year,
            'transmission': trans,
            'seat_number': seat,
            'fuel_type': fueltype,
            'name': name,
            'asset_no': assetno,
            'key_no': keyno,
            'body_colour': bodycolor,
            'license_type': licensetype,
            'kms_start': kmstart,
            'kms_current': kmcurrent,
            'availability_weekend': availweekend,
            'availability_afterhours': availafter,
            'comments': comments,
            'vehicle_cost': vehiclecost,
            'vehicle_cost_type': costtype
        }
        try:
            r = requests.post(url, headers=self.headers, json=body)
            if r.status_code in [200, '200', 201, '201']:
                print('success')
                return r.json()
            elif r.status_code in [401, '401', '400', 400]:
                print('not successful')
                return False
            else:
                print('failed to update data')
        except:
            print('Failed')

    def create_branch(self, name, slug, addrs, lat, lng, geohash, avabilityafterhours, avabilityweekends, businessstart, businessend):
        url = self.api_base + 'branch'
        body = {
            'name': name,
            'slug': slug,
            'addrs': addrs,
            'lat': lat,
            'long': lng,
            'geohash': geohash,
            'avaibility_afterhours': avabilityafterhours,
            'avaibility_weekends': avabilityweekends,
            'business_hours_start': businessstart,
            'business_hours_end': businessend
        }
        try:
            r = requests.post(url, headers=self.headers, json=body)
            if r.status_code in [201, '201']:
                print('Success')
                return(r.json())
            elif r.status_code in [401, '401']:
                print('Error {}'.format(str(r.status_code)))
                return False
            else:
                print('status code: {}'.format(str(r.status_code)))
        except:
            print('check script')

    def create_cc(self, name, code):
        url = self.api_base + 'cost-centre'
        body = {
            'name': name,
            'code': code
        }
        try:
            r = requests.post(url, headers=self.headers, json=body)
            if r.status_code in [201, '201']:
                print('Success')
                return(r.json())
            elif r.status_code in [401, '401']:
                print('Error {}'.format(str(r.status_code)))
                return False
            else:
                print('status code: {}'.format(str(r.status_code)))
        except:
            print('check script')

    def create_company(self, name, slug, connum, conemail, addrs, lat, lng, description, url, vehiclecost, costtype, currency, order, tolerance):
        url = self.api_base + 'company'
        body = {
            'name': name,
            'slug': slug,
            'contact_number': connum,
            'contact_email': conemail,
            'addrs': addrs,
            'lat': lat,
            'long': lng,
            'description': description,
            'url': url,
            'vehicle_cost': vehiclecost,
            'vehicle_cost_type': costtype,
            'currency': currency,
            'order_booking_rults_by': order,
            'booking_tolerance': tolerance
        }
        try:
            r = requests.post(url, headers=self.headers, json=body)
            if r.status_code in [201, '201', '200', 200]:
                print('Successfully created new rource status code {}'.format(
                    str(r.status_code)))
                return(r.json())
            elif r.status_code in [401, '401', 400, '400']:
                print('Error status code {}'.format(str(r.status_code)))
                return False
            else:
                print('error {}'.format(str(r.status_code)))
        except:
            print('error {}'.format(str(r.status_code)))

    def create_anything(self, a):  # a method for creating any rource
        url = self.api_base + str(a)
        body = {}
        try:
            r = requests.get(url, headers=self.headers, json=body)
            if r.status_code in [201, '201']:
                print('request successful')
                return(r.json())
            elif r.status_code in [401, '401']:
                print('Something is wrong with that request status code {}'.format(
                    str(r.status_code)))
                return False
            else:
                print('try again')
        except:
            print('no can do man')

    def update_vehicle(self, reg, year, trans, seat, fueltype, name, assetno, keyno, bodycolor, licensetype, kmstart, kmcurrent, availweekend, availafter, comments, vehiclecost, costtype):
        a = input('enter the enpoint for your vehicle: ')
        url = self.api_base + 'vehicle/' + a
        body = {
            'registration': reg,
            'year': year,
            'transmission': trans,
            'seat_number': seat,
            'fuel_type': fueltype,
            'name': name,
            'asset_no': assetno,
            'key_no': keyno,
            'body_colour': bodycolor,
            'license_type': licensetype,
            'kms_start': kmstart,
            'kms_current': kmcurrent,
            'availability_weekend': availweekend,
            'availability_afterhours': availafter,
            'comments': comments,
            'vehicle_cost': vehiclecost,
            'vehicle_cost_type': costtype
        }
        try:
            r = requests.put(url, headers=self.headers, json=body)
            if r.status_code in [200, '200', 201, '201']:
                print('success')
                return r.json()
            elif r.status_code in [401, '401', '400', 400]:
                print('not successful')
                return False
            else:
                print('failed to update data')
        except:
            print('Failed')

    def update_cc(self, name, code):
        url = self.api_base + 'cost-centre'
        body = {
            'name': name,
            'code': code
        }
        try:
            r = requests.put(url, headers=self.headers, json=body)
            if r.status_code in [201, '201']:
                print('Success')
                return(r.json())
            elif r.status_code in [401, '401']:
                print('Error {}'.format(str(r.status_code)))
                return False
            else:
                print('status code: {}'.format(str(r.status_code)))
        except:
            print('check script')

    def update_branch(self, name, slug, addrs, lat, lng, geohash, avabilityafterhours, avabilityweekends, businessstart, businessend):
        url = self.api_base + 'branch'
        body = {
            'name': name,
            'slug': slug,
            'addrs': addrs,
            'lat': lat,
            'long': lng,
            'geohash': geohash,
            'avaibility_afterhours': avabilityafterhours,
            'avaibility_weekends': avabilityweekends,
            'business_hours_start': businessstart,
            'business_hours_end': businessend
        }
        try:
            r = requests.put(url, headers=self.headers, json=body)
            if r.status_code in [201, '201']:
                print('Success')
                return(r.json())
            elif r.status_code in [401, '401']:
                print('Error {}'.format(str(r.status_code)))
                return False
            else:
                print('status code: {}'.format(str(r.status_code)))
        except:
            print('check script')

    def update_user(self, name, email, idnumb, contactnumber,
                    licensenumber, licenseexpmonth, licenseexpiryyear,
                    licensetype, liensecountry, ccid, activatedviacompanyid):
        a = input('Please tell me who you want to modify:  ')
        temp = self.api_base + 'user/' + str(a)
        body = {
            'name': name,
            'email': email,
            'employee_id': idnumb,
            'contact_number': contactnumber,
            'license_number': licensenumber,
            'license_expiry_month': licenseexpmonth,
            'license_expiry_year': licenseexpiryyear,
            'license_type': licensetype,
            'license_country': liensecountry,
            'cost-centre_id': ccid,
            'activated-via-company-id': activatedviacompanyid
        }
        try:
            r = requests.put(temp, json=body, headers=self.headers)
            if r.status_code in [401, '401']:
                print('failed to access the rource to update')
                return False
            elif r.status_code in [200, '200']:
                print('awesome, i have found it')
                return(r.json())
            else:
                print('Something is wrong, please check the script')
        except:
            print('Status code {}'.format(str(r.status_code)))

    def update_company(self, name, slug, connum, conemail, addrs, lat, lng, description, url, vehiclecost, costtype, currency, order, tolerance):
        url = self.api_base + 'company'
        body = {
            'name': name,
            'slug': slug,
            'contact_number': connum,
            'contact_email': conemail,
            'addrs': addrs,
            'lat': lat,
            'long': lng,
            'description': description,
            'url': url,
            'vehicle_cost': vehiclecost,
            'vehicle_cost_type': costtype,
            'currency': currency,
            'order_booking_rults_by': order,
            'booking_tolerance': tolerance
        }
        try:
            r = requests.put(url, headers=self.headers, json=body)
            if r.status_code in [201, '201', '200', 200]:
                print('Successfully created new rource status code {}'.format(
                    str(r.status_code)))
                return(r.json())
            elif r.status_code in [401, '401', 400, '400']:
                print('Error status code {}'.format(str(r.status_code)))
                return False
            else:
                print('error {}'.format(str(r.status_code)))
        except:
            print('error {}'.format(str(r.status_code)))
## delete rources
    def delete_anything(self,a):
        print("deleting rources now")
        url = self.api_base + str(a)
        user = input("Are you sure? y/n")
        if user in ['y','yes','ye','yeah','yep']:
            r = requests.delete(url,headers=self.headers)
            print("deleting rources {}".format(str(r.status_code)))
            return(r.status_code)
        else:
            print("No rources deleted")
            pass

    def __str__(self):
        pass

class dev(config):      ### dev sub class
    def __init__(self, host=None):      
        self.api_base = 'http://api.keaz.io/v1/'
        if host is None:
            self.host = 'keaz.keaz.io'
        else:
            self.host = host
        if not self.login():
            raise Exception
        self.headers = {'X-Source-Host': self.host,
                            'token': self.token}

class yoogo(config):
    def __init__(self, host=None):
        self.api_base = 'http://api.yoogoshare.com/v1/'
        if host is None:
            self.host = 'yoogo2.yoogoshare.com'
        else:
            self.host = host
        if not self.login():
            raise Exception
        self.headers = {'X-Source-Host': self.host,
                        'token': self.token}
        
































def main():
    data = yoogo()  # testing code here
    print(data.get_all_companies())


































if __name__ == '__main__':
    main()
