import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from common.logger import logger
from common.handler import dt, MAIL_CONTENT


class Mail:
    def __init__(self, domain, port, user, file_path):
        self.domain = domain
        self.port = port
        self.user = user
        self.file_path = file_path

    def get_message(self):
        if self.user is None:
            raise Exception('User not logged in')
        else:
            msg = MIMEMultipart()
            msg['from'] = self.user.username
            msg['subject'] = f'Work hours file Date: {dt}'
            msg['to'] = self.user.username
            msg.attach(MIMEText(MAIL_CONTENT, 'plain'))
            with open(self.file_path, 'r') as file:
                # Attach the file with filename to the email
                msg.attach(MIMEApplication(file.read(), Name=f'{file.name}'))
            return msg.as_string()

    def send_mail(self):
        try:
            message = self.get_message()
            session = smtplib.SMTP(f'smtp.{self.domain}.com', port=self.port)
            session.starttls()
            session.login(self.user.username, self.user.password)
            session.sendmail(self.user.username, self.user.username, message)
            session.quit()
        except Exception as err:
            logger.error(f'{repr(err)}')
        logger.info("Mail sent successfully")