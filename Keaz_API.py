import requests as req


class keaz:
    def __init__(self, host=None):
        self.baseurl = "http://api.keaz.software/v1/"
        if host is None:
            self.host = "keaz.keaz.software"
        else:
            self.host = host
        if not self.login():
           raise Exception
        self.headers = {'X-Source-Host': self.host, 'token': self.token}

    def login(self):
        print("Logging into Keaz....")
        password = input()
        form = {"email" : "john@keaz.co" , "password" : password }
        lh = {"login_headers": "", "HTTP": "X_Source-Host", "version": "1.40.0", "app_name": "KEAZ ACCESS STAGING",
            "content-type": "application/json", "device_type": "WEBSITE", "x_source_host": self.host}
        url = self.baseurl + "/login"
        print(lh)
        try:
            res = req.post(url=url, data=form, headers=lh)
            if res.status_code not in [200,'200']:
                print('Failed to login' + str(res.status_code))
                return False
            else:
                self.token = res.json()['token']
                return(True)
        except:
            print("failed to login, tough luck")
    def endpoint(self,path):
        print("Please enter your endpoint after the URL https://api.keaz.software/v1/: " )
        path = input()
        temp = self.baseurl + str(path)
        try:
            res = req.get(temp, headers = self.headers)
            if res.status_code in [200,'200']:
                print("Success: {}".format(str(res.status_code)))
                return(res.json())
            elif res.status_code in [400,'400']:
                print("Something went wrong {}".format(str(res.status_code)))
                return False
            else:
                print("Status code {}".format(str(res.status_code)))
        except:
            print("it didn't work")
    def bookings(self):
        number = input("enter your booking number: ")
        temp = self.baseurl + "booking/" + str(number)
        try:
            res = req.get(temp,headers = self.headers)
            if res.status_code in [200,'200']:
                print("Success {}".format(str(res.status_code)))
                return(res.json())
            elif res.status_code in [400,'400']:
                print("Error {}".format(str(res.status_code)))
                return False
            else:
                print("Error Code {}".format(str(res.status_code)))
        except:
            print("Error {}".format(str(res.status_code)))
    def branches(self):
        print("Please enter your Branch number to trace: ")
        a = input()
        temp = self.baseurl + "branch/" + str(a)
        try:
            res = req.get(temp,headers = self.headers)
            if res.status_code in [200,'200']:
                print("Success {}".format(str(res.status_code)))
                return(res.json())
            elif res.status_code in [400,'400']:
                print("Error {}".format(str(res.status_code)))
                return False
            else:
                print("Error Code {}".format(str(res.status_code)))
        except:
            print("Error {}".format(str(res.status_code)))
    def companies(self):
        print("Please enter your Company number to trace: ")
        a = input()
        temp = self.baseurl + "company/" + str(a)
        try:
            res = req.get(temp,headers = self.headers)
            if res.status_code in [200,'200']:
                print("Success {}".format(str(res.status_code)))
                return(res.json())
            elif res.status_code in [400,'400']:
                print("Error {}".format(str(res.status_code)))
                return False
            else:
                print("Error Code {}".format(str(res.status_code)))
        except:
            print("Error {}".format(str(res.status_code)))
        
    def users(self):
        a = input("Enter the User ID: ")
        temp = self.baseurl + "users/" + str(a)
        try:
            res = req.get(temp,headers = self.headers)
            if res.status_code in [200,'200']:
                print("Success {}".format(str(res.status_code)))
                return(res.json())
            elif res.status_code in [400,'400']:
                print("Error {}".format(str(res.status_code)))
                return False
            else:
                print("Error Code {}".format(str(res.status_code)))
        except:
            print("Error {}".format(str(res.status_code)))
    def getdata(self):
        a = input("enter your endpoint: ")
        temp = self.baseurl + str(a)
        try:
            res = req.get(temp,headers = self.headers)
            if res.status_code in [200,'200']:
                print("Success {}".format(str(res.status_code)))
                return(res.json())
            elif res.status_code in [400,'400']:
                print("Error {}".format(str(res.status_code)))
                return False
            else:
                print("Error Code {}".format(str(res.status_code)))
        except:
            print("Error {}".format(str(res.status_code)))

def main():
        pass
        ## used for testing functions

if __name__ == "__main__":
    main()
