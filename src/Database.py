
import mysql.connector


class Database():

    def __init__(self):
        self.information = {
            "Contacts_Database": mysql.connector.connect(
                host="localhost", user="root", passwd="", database="contacts")
        }

    def contactDatabase(self):
        return self.information['Contacts_Database']
