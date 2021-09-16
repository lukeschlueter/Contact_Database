import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=/tmp/mysql.sock;'
                      'Database=contacts;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM contacts')