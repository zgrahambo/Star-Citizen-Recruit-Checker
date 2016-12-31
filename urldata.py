import requests
import ast
import re


class RequestData:

    __url1 = "https://robertsspaceindustries.com/api/account/signin"
    __url2 = "https://robertsspaceindustries.com/account/referral-program"

    __headers = {"User-Agent": "Mozilla/5.0"}
    __remember = "0"
    __username = None
    __password = None
    __data = None
    __data2 = None
    __text = None
    __login_request = None
    __prospect_request = None
    __recruit_request = None

    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__data = {"username": username, "password": password, "remember": "0"}
        self.__data2 = "?recruits=1"

    def request_session(self):
        with requests.session() as session:
            self.__login_request = session.post(url=self.__url1, data=self.__data, headers=self.__headers)
            if self._check_login_success(self.__login_request.text) is True:
                self.__prospect_request = session.get(url=self.__url2)
                self.__recruit_request = session.get(url=(self.__url2 + self.__data2))
                return True
            else:
                return False

    def _check_login_success(self, text):
        text = text.replace("null", "None")
        data = ast.literal_eval(text)
        if data["success"] == 1:
            return True
        else:
            return False

    def get_prospects(self):
        if self.__prospect_request is not None:
            paragraph = re.findall(r'<div class="user">(.*?)<span>', str(self.__prospect_request.text))
            print("Your Prospects:")
            for eachP in paragraph:
                print(eachP)
        else:
            print("An error has occurred!")

    def get_recruits(self):
        if self.__recruit_request is not None:
            paragraph = re.findall(r'<div class="user">(.*?)<span>', str(self.__recruit_request.text))
            print("Your Recruits:")
            for eachP in paragraph:
                print(eachP)
        else:
            print("An error as occurred!")
