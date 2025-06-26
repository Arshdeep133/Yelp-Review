import pyodbc
from datetime import datetime
import pyinputplus as pyip



def search_user(conn, login, cur):
    print("\nSearch Users #########################################\n")
    print("Please enter the appropriate filters")
    
    user_name2 = ""
    while user_name2 == "":
        user_name2 = input("name of the user(or part of the name)")

    user_name = " ".join(user_name2.split())    
    useful = pyip.inputYesNo("userful(yes/no)")
    funny = pyip.inputYesNo("funny(yes/no)")
    cool = pyip.inputYesNo("cool(yes/no)")

    try:
        stmt = "SELECT user_id, name,useful, funny,cool,yelping_since  from user_yelp where name LIKE ?"

        if useful == 'yes':
            stmt += " and useful > 0"
        elif useful == 'no':
            stmt += " and useful = 0"
        if funny == 'yes':
            stmt += " and funny > 0"
        elif useful == 'no':
            stmt += " and funny = 0"
        if cool == 'yes':
            stmt += " and cool > 0"
        elif cool == 'no':
            stmt += " and cool = 0"
    
        cur.execute(stmt,"%" + user_name + "%" )

    
        result2 = cur.fetchall()
        if result2 != []:
            print ("{:<25} {:<20} {:<7} {:<7} {:<7} {:<30}".format('User_ID','Name','Useful','Funny','Cool', 'Date when the user registered at yelp'))
            for row in result2:
                User_id = row[0]
                name = row[1]
                useful1 = row[2]
                funny1 = row[3]
                cool1 = row[4]
                date = row[5]
                print("{:<25} {:<20} {:<7} {:<7} {:<7} {:<30}".format(User_id or "",name or "",str(useful1) or "",str(funny1) or "", str(cool1) or "",str(date) or ""))
    
        if result2 == []:
            print("There are such businesses that meet the above filter search criteria")
    except pyodbc.Error as e:
        conn.rollback()
        print("An error occurred:", e)

