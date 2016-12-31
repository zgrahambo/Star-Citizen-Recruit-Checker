import urldata


username = input("Username: ")
password = input("Password: ")

ud = urldata.RequestData(username=username, password=password)
if ud.request_session() is True:
    ud.get_prospects()
    ud.get_recruits()
else:
    print("Login request failed!")
