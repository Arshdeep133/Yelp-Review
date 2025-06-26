import pyodbc
import pyinputplus as pyip


def search_business(conn, login,cur):
    print("\nSearch Business #########################################\n")
    print("Please enter the appropriate filters")
    min_stars = pyip.inputInt('Please enter the minimum number of stars for the business:', min = 0, max = 5)
    max_stars = pyip.inputInt('Please enter the maximum number of stars for the business:', min = 0, max = 5)
    city2 = ""
    while city2 == "":
        city2 = input("Please enter the name of the city the business is located in:")
    
    city = " ".join(city2.split())


    business_name2 = ""
    while business_name2 == "":
        business_name2 = input("Please enter the name of the business (or part of the name):")

    business_name = " ".join(business_name2.split())

    try:

        stmt = cur.execute('SELECT business_id, name,address, city,stars  from business where city = ? and stars >= ? and stars <= ? and name LIKE ? order by name ASC', (city,min_stars,max_stars,"%" +business_name+"%") )
    

        result = cur.fetchall()
        if result != []:
            print ("{:<25} {:<50} {:<30} {:<20} {:<4}".format('Business_ID','Name','Address','City','Stars'))
            for row in result:
                business_id = row[0]
                name = row[1]
                address = row[2]
                city = row[3]
                stars = row[4]
                print("{:<25} {:<50} {:<30} {:<20} {:<4}".format(business_id or "",name or "",address or "",city or "", stars or ""))
        if result == []:
            print("There are such businesses that meet the above filter search criteria")

    except pyodbc.Error as e:
        conn.rollback()
        print("An error occurred:", e)
