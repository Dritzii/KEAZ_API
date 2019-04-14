'''
write a class based on KEAZ API for use
Author: John Pham
'''
import requests


class config(object):

    def __init__(self, host=None):  # constructor
        self.api_base = 'http://api.keaz.software/v1/'
        if host is None:
            self.host = 'keaz.keaz.software'
        else:
            self.host = host
        if not self.login():  # references def login(self)
            raise Exception and print("Login not successful")
        self.headers = {'X-Source-Host': self.host,
                        'token': self.token}
        print(host)
        print(self.headers)


    def login(self):
        print('Logging in')
        headers = {'X-Source-Host': self.host,
                   'app_name': 'Johns Script',
                   'version': '1.40.0',
                   'device_type': 'SCRIPT'} 
        #pw = input('Enter your password for Keaz API: ')
        form = {'email': 'john@keaz.co',
                'password': 'Aqualite12@'}  # pw}
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
            elif r.status_code in [400, '400']:
                print('Something is wrong with that request status code {}'.format(
                    str(r.status_code)))
                return False
            elif r.status_code in [404, '404']:
                print("Server has been contacted successfully, but it hasn't been able to find the resources given reason: {}".format(str(r.status_reason)))
                return False
            elif r.status_code in [504, '504',500,'500']:
                print("Server has been timed out: {}".format(str(r.status_reason)))
                return False
            else:
                print('try again {}'.format(str(r.status_code)))
        except:
            print('no can do man {}'.format(str(r.reason)))

### importing csv file and iterate with POST request
    def import_file(self, a):
        file = open(a, 'r')
        import csv
        reader = csv.reader(file)
        reader.__next__()
        for each in reader:
            yield each


    def get_inactive_vehicles(self,page):
        url = self.api_base + 'vehicles?inactive={}'.format(str(page))
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code in [200, '200']:
                print('Successfully grabbed data {}'.format(str(r.status_code)))
                return(r.json())
            elif r.status_code in [400,'400']:
                print('Error with that request {}'.format(str(r.status_code)))
                return False
            elif r.status_code in [404, '404']:
                print("Server has been contacted successfully, but it hasn't been able to find the resources given reason: {}".format(str(r.status_reason)))
                return False
            else:
                print('error {}'.format(str(r.status_code)))
                return False
        except:
            print('error')


    def get_locations(self):
        url = self.api_base + 'locations/cities'
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code in [200, '200']:
                print('You have successfully grabbed data in {}'.format(
                    str(r.status_code)))
                return(r.json())
            elif r.status_code in [400, '400']:
                print('Error status code {}'.format(str(r.status_code)))
                return False
            elif r.status_code in [404, '404']:
                print("Server has been contacted successfully, but it hasn't been able to find the resources given reason: {}".format(str(r.status_reason)))
                return False
            else:
                print('A different error {}'.format(str(r.reason)))
        except:
            print('Error')


    def get_location_activities(self,number,symd,start,eymd,end):
        url = self.api_base + 'activities/city/{}'.format(str(number)) + '/{}'.format(str(symd)) + '/{}'.format(str(start)) + '/{}'.format(str(eymd)) + '/{}'.format(str(end))
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code in [200, '200']:
                print('You have successfully grabbed data in {}'.format(
                    str(r.status_code)))
                return(r.json())
            elif r.status_code in [400, '400']:
                print('Error status code {}'.format(str(r.status_code)))
                return False
            elif r.status_code in [404, '404']:
                print("Server has been contacted successfully, but it hasn't been able to find the resources given reason: {}".format(str(r.status_reason)))
                return False
            else:
                print('A different error {}'.format(str(r.reason)))
        except:
            print('Error')


    def get_sms(self,kit,symd,start,eymd,end):
        url = self.api_base + 'vehicle/kit/{}/sms_logs'.format(str(kit)) + '/{}'.format(str(symd)) + '/{}'.format(str(start)) + '/{}'.format(str(eymd)) + '/{}'.format(str(end))
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code in [200, '200']:
                print('You have successfully grabbed data in {}'.format(
                    str(r.status_code)))
                return(r.json())
            elif r.status_code in [400, '400']:
                print('Error status code {}'.format(str(r.status_code)))
                return False
            elif r.status_code in [404, '404']:
                print("Server has been contacted successfully, but it hasn't been able to find the resources given reason: {}".format(str(r.status_reason)))
                return False
            else:
                print('A different error {}'.format(str(r.reason)))
        except:
            print('Error')

            ### serial number for scans - gets queried from mongodb
    def get_scan(self,serial,symd,start,end):
        url = self.api_base + 'udp_logs/{}'.format(str(serial)) + '/{}'.format(str(symd)) + '/{}'.format(str(start)) +  '/{}'.format(str(end))
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code in [200, '200']:
                print('You have successfully grabbed data in {}'.format(
                    str(r.status_code)))
                return(r.json())
            elif r.status_code in [400, '400']:
                print('Error status code {}'.format(str(r.status_code)))
                return False
            elif r.status_code in [404, '404']:
                print("Server has been contacted successfully, but it hasn't been able to find the resources given reason: {}".format(str(r.status_reason)))
                return False
            else:
                print('A different error {}'.format(str(r.status_code)))
        except:
            print('Error')


    def company_activities(self,id,start,stime,end,etime):
        url = self.api_base + 'activities/company/{}/'.format(str(id)) + start + '/' + stime + '/' + end + '/' + etime
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code in [200, '200']:
                print('You have successfully grabbed data in {}'.format(
                    str(r.status_code)))
                return(r.json())
            elif r.status_code in [400, '400']:
                print('Error status code {}'.format(str(r.status_code)))
                return False
            elif r.status_code in [404, '404']:
                print("Server has been contacted successfully, but it hasn't been able to find the resources given reason: {}".format(str(r.status_reason)))
                return False
            else:
                print('A different error {}'.format(str(r.status_code)))
        except:
            print('Error')


    def get_login_history(self,symd,eymd,start,end):
        url = self.api_base + 'logins/{}'.format(str(symd)) + '/{}'.format(str(start)) + '/{}'.format(str(eymd)) +  '/{}'.format(str(end))
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code in [200, '200']:
                print('You have successfully grabbed data in {}'.format(
                    str(r.status_code)))
                return(r.json())
            elif r.status_code in [400, '400']:
                print('Error status code {}'.format(str(r.status_code)))
                return False
            elif r.status_code in [404, '404']:
                print("Server has been contacted successfully, but it hasn't been able to find the resources given reason: {}".format(str(r.status_reason)))
                return False
            else:
                print('A different error {}'.format(str(r.status_code)))
        except:
            print('Error')

#### use this api for CoC

    def get_all_bookings(self,id,start,stime,end,etime):
        url = self.api_base + '/company' + '/{}'.format(str(id)) + 'paging_bookings/' + start + '/' + stime + '/' + end + '/' + etime
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code in [200, '200']:
                print('Request Successful')
                return(r.json())
            elif r.status_code in [400,'400']:
                print('Something is wrong status code: {}'.format(str(r.status_code)))
                return False
            elif r.status_code in [404, '404']:
                print("Server has been contacted successfully, but it hasn't been able to find the resources given reason: {}".format(str(r.status_reason)))
                return False
            elif r.status_code in [504,'504',500,'500',502,'502']:
                print("Server time out")
                return False
            else:
                print('Error {}'.format(str(r.status_code)))
        except:
            print('sorry status code {}'.format(str(r.reason)))


    def get_all_cancelled_bookings(self,id,start,stime,end,etime):
        url = self.api_base + '/company' + '/{}'.format(str(id)) + 'bookings/cancelled/' + start + '/' + stime + '/' + end + '/' + etime
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code in [200, '200']:
                print('Request Successful')
                return(r.json())
            elif r.status_code in [400,'400']:
                print('Something is wrong status code: {}'.format(str(r.status_code)))
                return False
            else:
                print('Error {}'.format(str(r.status_code)))
        except:
            print('sorry status code {}'.format(str(r.reason)))


    def get_all_cancelled_paging_bookings(self,id,start,stime,end,etime):
        url = self.api_base + '/company' + '/{}'.format(str(id)) + 'paging_bookings/cancelled/' + start + '/' + stime + '/' + end + '/' + etime
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code in [200, '200']:
                print('Request Successful')
                return(r.json())
            elif r.status_code in [400,'400']:
                print('Something is wrong status code: {}'.format(str(r.status_code)))
                return False
            else:
                print('Error {}'.format(str(r.status_code)))
                return False
        except:
            print('sorry status code {}'.format(str(r.reason)))


    def get_all_inactive_users(self):
        i = 0
        url = self.api_base + 'users/{}?inactive=1'.format(str(i))
        r = requests.get(url,headers=self.headers)
        if r.status_code in [200,'200']:
            print("Successful request")
            pgcount = r.json()['total_page']
            for page in range(1, pgcount):
                print(r.json())
        elif r.status_code in [400,'400']:
            print("something is wrong")
            return(False)
        else:
            print("not successful")
            return(False)
       
    def get_user_bookings(self,id,start,stime,end,etime):
        url = self.api_base + '/user' + '/{}'.format(str(id)) + 'paging_bookings/' + start + '/' + stime + '/' + end + '/' + etime
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code in [200, '200']:
                print('Request Successful')
                return(r.json())
            elif r.status_code in [400,'400']:
                print('Something is wrong status code: {}'.format(str(r.status_code)))
            else:
                print('Error {}'.format(str(r.status_code)))
        except:
            print('sorry status code {}'.format(str(r.reason)))


    def get_booking(self,a):
        ### a = input('Enter the booking number: ')
        url = self.api_base + 'booking/' + str(a)
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code in [200, '200']:
                print('request successful')
                return(r.json())
            elif r.status_code in [400, '400']:
                print('Something is wrong status code {}'.format(
                    str(r.status_code)))
                return False
            else:
                print('no can do')
        except:
            print('sorry status code {}'.format(str(r.reason)))


    def get_open_bookings(self,id,start,stime,end,etime):
        url = self.api_base + '/company/{}/paging_bookings/open'.format(str(id)) + '/' + start + '/' + stime + '/' + end + '/' + etime
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code in [200, '200']:
                print('Request Successful')
                return(r.json())
            elif r.status_code in [400,'400']:
                print('Something is wrong status code: {}'.format(str(r.status_code)))
            else:
                print('Error {}'.format(str(r.status_code)))
        except:
            print('sorry status code {}'.format(str(r.reason)))


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


    def get_all_costcentre(self):
        url = self.api_base + 'cost-centres'
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


    def get_kits(self):
        url = self.api_base + 'kits'
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
## need to add inactive kits to code ++++

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
# creating resources below

    def create_user(self, name, email, idnumb, contactnumber,
                    licensenumber, licenseexpmonth, licenseexpiryyear,
                    licensetype, liensecountry, ccid, activatedviacompanyid):
        url = self.api_base + 'user'
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
            if r.status_code in [400, '400']:
                print('failed to access the resource to update{}'.format(str(r.status_code)))
                return False
            elif r.status_code in [401, '401']:
                print('bad request{}'.format(str(r.status_code)))
                return False
            elif r.status_code in [201,'201',200,'200']:
                print('request accepted, code: {}'.format(str(r.status_code)))
                return r.status_code
            else:
                print('Something is wrong, please check the script')
        except:
            print('Status code {}'.format(str(r.status_code)))

### double check the JSON for creating bookings required with each update.
    def create_booking(self, date, branch, user_id, vehicle, cost_centre, trip_purpose, starttime, startdate, enddate, endtime):
        url = self.api_base + 'booking'
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
            'start_timezone_offset': -36000, ## dependant on client timezone
            'end_timezone_offset': -36000,
            'drop_off_branch_id': branch,
            'start_time': starttime,   
            'start_date':  startdate, 
            'end_date': enddate,
            'end_time': endtime,
            'vehicle_id': vehicle
        }
        print(url)
        print(payload)
        try:
            r = requests.post(
                url, data=payload, headers=self.headers)
            if r.status_code in [201, '201', 200, '200']:
                print('Completed your update {}'.format(str(r.status_code)))
                return r.status_code
            elif r.status_code in [401, '401', 400, '400']:
                print('failed to initialize {}'.format(str(r.status_code)))
                return False
        except:
            print('failed to update:  ' + ' ' + str(r.status_code))


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
                return r.status_code
            elif r.status_code in [401, '401', '400', 400]:
                print('not successful{}'.format(str(r.status_code)))
                return False
            else:
                print('failed to create data')
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
            if r.status_code in [201, '201',200,'200']:
                print('Success')
                return(r.status_code)
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


    def create_anything(self, a):  # a method for creating any resource
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
    # update resources below


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
            if r.status_code in [200, '200']:
                print('Success')
                return(r.json())
            elif r.status_code in [401, '401']:
                print('Error {}'.format(str(r.status_code)))
                return False
            else:
                print('status code: {}'.format(str(r.status_code)))
        except:
            print('check script')


    def update_branch(self,id, name, slug, addrs, lat, lng, geohash, avabilityafterhours, avabilityweekends, businessstart, businessend):
        url = self.api_base + 'branch/{}'.format(str(id))
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
            if r.status_code in [200, '200']:
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
            if r.status_code in ['200', 200]:
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


    def update_anything(self,a,body):
        body = body
        print('Updating anything')
        url = self.api_base + str(a)
        try:
            r = requests.put(url, headers=self.headers, json=body)
            if r.status_code in ['200', 200]:
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

# delete rources below
    def delete_branches(self,a):
        print('deleting branches now {}'.format(str(a)))
        url = self.api_base + 'branch/' + str(a)
        user = input('Are you sure? y/n')
        try:
            if user in ['y', 'yes', 'ye', 'yeah', 'yep']:
                r = requests.delete(url, headers=self.headers)
                print('deleting rources {}'.format(str(a)))
                return(r.status_code)
            else:
                print('No resources deleted')
                pass
        except Exception as err:
            print('error {}'.format(str(err)))


    def delete_anything(self, a):
        print('deleting resources now')
        url = self.api_base + str(a)
        user = input('Are you sure? y/n')
        try:
            if user in ['y', 'yes', 'ye', 'yeah', 'yep']:
                r = requests.delete(url, headers=self.headers)
                print('deleting rources {}'.format(str(a)))
                return(r.status_code)
            else:
                print('No resources deleted')
                pass
        except Exception as err:
            print('error {}'.format(str(err)))


    def delete_company(self, a):
        print('deleting resources now')
        url = self.api_base + 'company/' + str(a)
        user = input('Are you sure? : y/n')
        if user in ['y', 'ye', 'yes', 'yep', 'yeah']:
            r = requests.delete(url, headers=self.headers)
            print('deleting resources now for {}'.format(str(a)))
            return r.status_code
        else:
            print('no resources deleted')
            return False


    def delete_users(self, a):
        print('Attempting to delete resources')
        url = self.api_base + 'users/' + str(a)
        user = input('Are you sure? : y/n')
        if user in ['y', 'ye', 'yes', 'yep', 'yeah']:
            r = requests.delete(url, headers=self.headers)
            print('deleting resources now for {}'.format(str(a)))
            return r.status_code
        else:
            print('no resources deleted')
            return False


    def delete_booking(self,a):
        print('Attempting to delete booking number {}'.format(str(a)))
        url = self.api_base + 'booking/{}'.format(str(a))
        user = input('Are you sure? : y/n')
        if user in ['y', 'ye', 'yes', 'yep', 'yeah']:
            r = requests.delete(url, headers=self.headers)
            print('deleting resources now for {}'.format(str(a)))
            return r.status_code
        else:
            print('no resources deleted')
            return False

### delete functions have a prompt for user to delete
    def delete_vehicles(self, a):
        print('Attempting to delete resources')
        url = self.api_base + 'vehicles/' + str(a)
        user = input('Are you sure? : y/n')
        if user in ['y', 'ye', 'yes', 'yep', 'yeah']:
            r = requests.delete(url, headers=self.headers)
            print('deleting resources now for {}'.format(str(a)))
            return r.status_code
        else:
            print('no resources deleted')
            return False

    def __str__(self):
        pass


class dev(config):  # dev sub class inheritance from config class
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


class yoogo(config):  # yoogo sub class
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
    """
    def import_user_file():
        import csv
        file = open('C:/Users/John Pham/Documents/GitHub/KEAZ_API/ccc.csv','r')
        reader = csv.reader(file)
        reader.__next__()
        for each in reader:
            yield each
    
        for each in import_user_file():
            print(each)
    """
    data = config('envoy-there.keaz.software') # enter sourcehost here
    """
    for each in import_user_file():
        body = {"security_code": each[0]}
        _id = each[1]
check slug tomorrow ###
    """

    updates = data.get_all_inactive_users()
    print(updates)

    """
    for user in updates:
        try:
            print(user)
        except UnicodeDecodeError:
            print("Unicode Errror")

"""


if __name__ == "__main__":
    main()


