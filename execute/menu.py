from common.menuOpt import MenuOpt
from models.login import Login
from models.mail import Mail
from models.status import Status
from models.user import User
from models.enterShift import EnterShift
from common.handler import *


def login():
    data = Login(file_path + certificate)
    return data.log_in()


def enter_shift():
    new_shift = EnterShift(file_path + work_name)
    new_shift.enter_new_shift()


def view_status():
    current_status = Status(file_path + work_name)
    current_status.show_status()


def send_mail(user):
    export = Mail(domain=domain, port=port, user=user, file_path=file_path + work_name)
    export.send_mail()


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
            if choice == MenuOpt.LOGIN.value:
                user_details = login()
                user = User(user_details["username"], user_details["password"])
            elif choice == MenuOpt.ENTER_SHIFT.value:
                enter_shift()
            elif choice == MenuOpt.CURRENT_STATUS.value:
                view_status()
            elif choice == MenuOpt.SEND_MAIL.value:
                send_mail(user)
            else:
                exit(0)
    except Exception as err:
        logger.error(f'Error has occur {repr(err)}')

    finally:
        exit(0)


if __name__ == "__main__":
    main_menu()
