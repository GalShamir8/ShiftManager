import smtplib
from common.menuOpt import MenuOpt
from models.login import Login
from models.user import User
from models.enterShift import EnterShift

file_path = "C:\WorkShifts"
work_name = "\QuaDream.csv"
certificate = "\certificate.json"
domain = "Gmail"


def login():
    data = Login(file_path + certificate)
    return data.log_in()


def enter_shift():
    new_shift = EnterShift(file_path + work_name)
    new_shift.enter_new_shift()


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
            if choice == MenuOpt.LOGIN:
                user_details = login()
                user = User(user_details["username"], user_details["password"])
            elif choice == MenuOpt.ENTER_SHIFT:
                enter_shift()
            elif choice == MenuOpt.CURRENT_STATUS:
                view_status()
            elif choice == MenuOpt.SEND_MAIL:
                send_mail(user)
            else:
                exit(0)
    except Exception as err:
        print(f'Error has occur {repr(err)}')

    finally:
        exit(0)


if __name__ == "__main__":
    main_menu()
