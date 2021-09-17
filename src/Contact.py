
from validate_email import validate_email
is_valid = validate_email('example@example.com')


class Contact():

    def __init__(self):
        self.information = {
            "first_name": input("What is your first name?\n"),
            "last_name": input("What is your last name?\n"),
            "phone_number": input("What is your phone number?\n"),
            "email": self.checkEmail()
        }

    def addContact(self):
        return ("INSERT INTO contacts "
                "(first_name, last_name, phone_number, email) "
                f"VALUES ('{self.information['first_name']}', '{self.information['last_name']}', "
                f"'{self.information['phone_number']}', '{self.information['email']}')")

    def checkEmail(self):
        is_valid = False
        while not is_valid:
            email = input("What is your email?\n")
            is_valid = validate_email(email)
        return email
