import json
import os
from common.handler import check_valid_mail

class Login:
    def __init__(self, file_path):
        self.file_path = file_path
        self.isExist = os.path.exists(self.file_path)

    def log_in(self):
        if self.isExist:
            with open(self.file_path, ) as jsonfile:
                data = json.load(jsonfile)
                username = data["username"]
                password = data["password"]
                return data
        else:
            data = {}
            username = None
            while not check_valid_mail(username):
                username = input("Enter your Email:")
            password = input("Enter your password: ")
            data["username"] = username
            data["password"] = password
            with open(self.file_path, mode='w') as jsonfile:
                json.dump(data, jsonfile)
                print(f'\nSaved successfully to file: {self.file_path}\n')

            return data
