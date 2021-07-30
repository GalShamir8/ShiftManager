import datetime
import re

header = ["Date", "Day", "Start hour", "Exit Hour", "Total Hours"]
dt = datetime.datetime.today()

'''Function for checking validate mail
   return True/False accordingly '''


def check_valid_mail(username):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if username is None:
        return False
    valid = re.match(regex, username)
    if not valid:
        print("Invalid mail, please enter again")
    return valid


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
