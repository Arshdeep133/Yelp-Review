import pyodbc
import pyinputplus as pyip
from search_user import search_user 


def make_friend(conn, login, cur):
    print("\nMake Friend #########################################\n")

    print("Please select from the following options: ")
    print("1. Search for the user id to create friendship.")
    print("2. Enter the user id")
    option = pyip.inputInt(" Enter your choice: ", min = 1, max = 2)

    if(option == 1):
        search_user(conn, login, cur)
    
    friend_id = ""
    while friend_id == "":
        friend_id = input("Please enter the user's id to create a friendship: \n")


    try:

        stmt = cur.execute("INSERT INTO friendship(user_id, friend) values (?,?)", (login,friend_id )).rowcount

        conn.commit()

        if (cur.rowcount != 0):
            print("Friendship has been created")

        else: 
            print("Friendship cannot be created. Either because the friendship already exist or the user id to create friend is not valid")
    except pyodbc.Error as e:
        conn.rollback()
        print("An error occurred:", e)
