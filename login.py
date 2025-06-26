import pyodbc
from search_business import search_business
from search_user import search_user
from make_friend import make_friend
from write_review import write_review
import pyinputplus as pyip

def loginp(conn, cur):
    login = ""
    while login == "":
        login = input("\nPlease enter the login: \n")

    try:
        num = cur.execute('SELECT * from user_yelp where user_id = ?', (login))
        row = cur.fetchone()
        if row is None:
            print("Enter valid user_id")
            loginp(conn, cur)
        else:
            print("Login Successful ")
            operations(conn,login, cur)

    except pyodbc.Error as e:
        conn.rollback()
        print("An error occurred:", e)



def operations(conn, login, cur):
    while True:
        print("\nPlease select what you want to do from the following: #########################################\n")
        print("1. Search Business")
        print("2. Search Users")
        print("3. Make Friend")
        print("4. Write Review")
        print("5. Exit the Program")
        operation = pyip.inputInt("Enter the selection number: ", min = 1, max = 5)
        if operation == 1:
            search_business(conn, login, cur)
        elif operation == 2:
            search_user(conn, login, cur)
        elif operation == 3:
            make_friend(conn, login, cur)
        elif operation == 4:
            write_review(conn, login, cur)
        else:
            exit()



    

