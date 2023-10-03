
import mysql.connector
from prettytable import PrettyTable, from_db_cursor


print("-"*40)
print(f"\n    Welcome to 4group For Cars Rental") 
print('\n',"-"*40,'\n')  

 
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='your user name',
    db='add data base name'
)

m = connection.cursor()
m.execute("select Vehicle_id, Model, Year, Daily_price from yourdatabase.yourtable")
mytable = from_db_cursor(m)
print(mytable,'\n')
###############  we need to check if he choose the right id 
user_choise = int(input("Please enter Vehicle_id you would like to rent:\n"))  
m.execute(f"select available from yourdatabase.yourtable where Vehicle_id = {user_choise}")
 
myresult = m.fetchone()
if myresult[0] > 0 : # he can rent 
    
    print("Please full the below form:")
    fname = input("First name:\n") 
    lname = input("Last name:\n") 
    license = input("Driver license:\n") 
