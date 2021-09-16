
import mysql.connector
from Contact import Contact
from Database import Database

contact = Contact()
database = Database()


mycursor = database.contactDatabase().cursor()

mycursor.execute(contact.addContact())

# Make sure data is committed to the database
database.contactDatabase().commit()
mycursor.close()
database.contactDatabase().close()
