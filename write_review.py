import pyodbc
import pyinputplus as pyip
import string
import random

def ran(conn, cur):
    charlist = string.ascii_letters + string.digits +'-'+'_'
    rand = ""
    i = 22

    while i != 0:
        rand = rand + random.choice(charlist)
        i -= 1
    

    rando = cur.execute("select * from review where review_id = ?", rand)

    res = cur.fetchall()

    if res == []:
        return rand
    else:
        rando(conn, cur)


     
def write_review(conn, login, cur):
    print("\nWrite Review #########################################\n")

    ID_buss = ""
    while ID_buss == "":
        ID_buss = input("Please enter the id of business for which you want to write the review: ")

    star = pyip.inputInt("Please enter the number of stars for the business: ", min = 1, max = 5)


    review_id = ran(conn, cur)   
    
    try:

       stmt = cur.execute("Insert into review(review_id, user_id, business_id, stars) values (?,?,?,?)", (review_id,login, ID_buss,star)).rowcount

       conn.commit()

       if (cur.rowcount != 0):
            print("Review has been added succesfully")
       else:
            print("The review cannot be saved as the business_id is Invalid")

    except pyodbc.Error as e:
        conn.rollback()
        print("An error occurred:", e)
    


