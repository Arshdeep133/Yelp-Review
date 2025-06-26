import pyodbc
import datetime
from login import loginp

conn = pyodbc.connect('driver={ODBC Driver 18 for SQL Server};server=cypress.csil.sfu.ca;uid=s_aka232;pwd=2nT7aA2T4GY6Q6mb;Encrypt=yes;TrustServerCertificate=yes')

cur = conn.cursor()

# to validate the connection, there is no need to change the following line
cur.execute( 'SELECT username from dbo.helpdesk' )
row = cur.fetchone ()

while row:
    print ( 'SQL Server standard login name = ' + row [ 0 ] )
    row = cur.fetchone ()

loginp(conn, cur)

cur.close()
conn.close()

