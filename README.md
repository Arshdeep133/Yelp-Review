# Yelp-Review

Libraries required for the applica􀆟on:
1. pyinputplus: For input validation. To install run the following command in the terminal.
pip install pyinputplus
2. The rest of the libraries that I used are already inbuilt in visual studio code.
* string
* random
* date􀆟me
* pyodbc
Please run connec􀆟on.py to test the applica􀆟on.


## Overview:
The application is a command line interface applica􀆟on wri􀆩en in python3. You do not need to recompile
the application to test each func􀆟onality as it does not close on its own, you must select the op􀆟on ‘Exit
the program’ to exit. A􀅌er running every func􀆟on, you will get the op􀆟ons again to test the other
functionalities.
The function is passed the login, cursor, and connec􀆟on so that the func􀆟ons can access the SQL. The
func􀆟ons do the input valida􀆟on for all the user inputs.
It contains the following files.
1. connec􀆟on.py: This is this the file that will run the applica􀆟on as it contains the connec􀆟on required
and it prompt the use for the login
2. login.py: Contains the implementa􀆟on of the login func􀆟on and the selec􀆟on menu func􀆟on that will
give the users with the op􀆟ons to test different functionalities
3. search_business.py: Contain the implementa􀆟on of search business functionality
4. search_user.py: Contain the implementa􀆟on of search user functionality
5. make_friend.py: contain the implementa􀆟on of the make friend functionality
6. write_review.py: contain the implementa􀆟on of the write review functionality
