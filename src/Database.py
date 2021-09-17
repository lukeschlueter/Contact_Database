
import mysql.connector

'''
Created Sept 17, 2021

@author Luke Schlueter
'''


class Database():

    def __init__(self):
        self.information = {
            "Contacts_Database": mysql.connector.connect(
                host="localhost", user="root", passwd="", database="contacts")
        }

    def contactDatabase(self):
        return self.information['Contacts_Database']
