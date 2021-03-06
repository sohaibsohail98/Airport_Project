from Database_Connection.database_connection import DatabaseConnector
from Interfacer import Interfacer
import pyodbc
import os

database_link = DatabaseConnector("databases.spartaglobal.academy", "JMS_AirportDatabase", "SA",
                                  "Passw0rd2018")  # create instance with credentials
connection = database_link.establish_connection()  # Use instance to establish connection

# Current ERROR - run 1 = blank output / run 2 = error output / run 3 = successful output
# This try helps us to quickly decipher if the database has returned the correct data, if not we can quickly reset the
# run instance. This is a bug that is occurring with the organisations DBMS (Azure)
try:
    print("-"*80)
    print(" "*30, "Existing Flight")
    print("-"*80)
    rows = connection.execute('SELECT * FROM Flights')
    for row in rows:
        print(row)
except pyodbc.ProgrammingError:
    exit("Due to a current bug we could not connect, rerun program.")  # end program

# Start Program Flow
start = Interfacer(connection)
start.choose_interface()
