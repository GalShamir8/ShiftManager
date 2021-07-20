import csv
import os.path
import datetime
import json
import re
import smtplib
from User import User
import getpass

file_path = "C:\WorkShifts"
work_name = "\QuaDream.csv"
certificate = "\certificate.json"
domain = "Gmail"

header = ["Date", "Day", "Start hour", "Exit Hour", "Total Hours"]
dt = datetime.datetime.today()


# @return True if the start hour is smaller then end hour else False
def check_start_hour(start_hour, end_hour):
    return int(start_hour[0]) < int(end_hour[0]) or (
            int(start_hour[0]) == int(end_hour[0]) and int(start_hour[1]) < int(end_hour[1]))


# calculate total shift hours
# @return tuple -> (hours,minutes)
def calc_hours(start_hour, end_hour):
    if not int(end_hour[0]) == int(start_hour[0]):
        total_hours = (int(end_hour[0]) - int(start_hour[0]), (int(end_hour[1])) - int(start_hour[1])) if (
                int(end_hour[0]) > int(start_hour[0]) and int(end_hour[1]) >= int(start_hour[1])) else (
            (int(end_hour[0]) - int(start_hour[0]) - 1, int(start_hour[1]) - int(end_hour[1])))
        return total_hours
    elif int(end_hour[0]) < int(start_hour[0]):
        return 0, int(start_hour[1]) - int(end_hour[1])
    else:
        return 0, int(end_hour[1]) - int(start_hour[1])


def get_hours():
    try:
        while True:
            start_hour = input("Enter Start Hour: (Format -> Hours:Minutes) ")
            # start_hour[0] = hours, start_hour[1] = minutes
            start_hour = start_hour.split(sep=':')
            if int(start_hour[0]) >= 0 and int(start_hour[1]) >= 0:
                end_hour = input("Enter End Hour: (Format -> Hours:Minutes) ")
                # end_hour[0] = hours, end_hour[1] = minutes
                end_hour = end_hour.split(sep=':')
                if int(end_hour[0]) < 0 or int(end_hour[1]) < 0:
                    print("Hour can't contain negative values")
                elif not check_start_hour(start_hour, end_hour):
                    print("Start hour can't be larger then end hour")
                else:
                    return start_hour, end_hour
            else:
                print("Hour can't contain negative values")

    except Exception as err:
        raise err


def update_table(writer):
    try:
        hours = get_hours()
        total_hours = calc_hours(hours[0], hours[1])
        values = [dt.strftime("%d/%m/%y"), dt.now().strftime("%A"), f'{hours[0][0]} : {hours[0][1]}',
                  f'{hours[1][0]} : {hours[1][1]}', f'{str(total_hours[0])} : {str(total_hours[1])}']
        file_dict = {}
        for field, value in zip(header, values):
            file_dict[field] = str(value)

        writer.writerow(file_dict)
    except Exception as err:
        print(repr(err))


# Function for checking validate mail
# @ return True/False accordingly
def check_valid_mail(username):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if username is None:
        return False
    valid = re.match(regex, username)
    if not valid:
        print("Invalid mail, please enter again")
    return valid


def login():
    # check if the file already exist

    if os.path.exists(file_path + certificate):
        with open(file_path + certificate, ) as jsonfile:
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
        with open(file_path + certificate, mode='w') as jsonfile:
            json.dump(data, jsonfile)
            print(f'\nSaved successfully to file: {file_path + certificate}\n')

        return data


def enter_shift():
    fileExist = os.path.exists(file_path + work_name)
    mode = 'w' if not fileExist else 'a'
    with open(file_path + work_name, mode=mode, newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        if not fileExist:
            writer.writeheader()
        try:
            update_table(writer)
            print(f'\nSaved successfully to file: {file_path + work_name}\n')
        except Exception as err:
            print(f'{repr(err)}')


def view_status():
    pass


def send_mail(user):
    session = smtplib.SMTP(f'smtp.{domain}.com', port=587)
    session.ehlo()
    session.starttls()

def main_menu():
    print("Welcome to the shift manager")
    user = None
    try:
        while True:
            choice = int(input(f'Choose from the following menu, press any key to exit:\n'
                               f'1 -> Login or Sign Up\n'
                               f'2 -> Enter New Shift\n'
                               f'3-> View Current Hours Status\n'
                               f'4 -> Export To Mail\n'
                               f'Enter your choice: '))
            if choice == 1:
                user_details = login()
                user = User(user_details["username"], user_details["password"])
            elif choice == 2:
                enter_shift()
            elif choice == 3:
                view_status()
            elif choice == 4:
                send_mail(user)
            else:
                exit(0)
    except Exception as err:
        print(f'Error has occur {repr(err)}')

    finally:
        exit(0)


if __name__ == "__main__":
    main_menu()
