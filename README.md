# Yelp-Review CLI Application

## Overview
Yelp-Review is a **command-line interface (CLI) application** written in Python 3 that allows users to interact with a simulated Yelp-like system. The application supports functionalities such as searching for businesses, searching for users, making friends, and writing reviews.  

The program remains active until the user chooses **“Exit the program”**, allowing you to test multiple functionalities in a single session. All user inputs are validated to ensure smooth interaction with the SQL database.  

---

## Features
- **Login system**: Securely authenticate users.  
- **Search Business**: Look up businesses in the database.  
- **Search User**: Find other users by username or other attributes.  
- **Make Friend**: Send friend requests or connect with other users.  
- **Write Review**: Submit reviews for businesses.  

Each function receives the login, cursor, and connection objects so it can interact with the SQL database seamlessly.  

---

## File Structure
| File | Description |
|------|-------------|
| `connection.py` | Entry point of the application. Handles database connection and prompts user login. Run this file to start the app. |
| `login.py` | Implements the login functionality and displays the selection menu for testing different functionalities. |
| `search_business.py` | Implements the “search business” functionality. |
| `search_user.py` | Implements the “search user” functionality. |
| `make_friend.py` | Implements the “make friend” functionality. |
| `write_review.py` | Implements the “write review” functionality. |

---

## Prerequisites
The following Python libraries are required:  

- **pyinputplus** (for input validation)  
  Install via terminal:
  ```bash
  pip install pyinputplus

Built-in Python libraries (no installation required):

- **string**
- **random**
- **datetime**
- **pyodbc**


## How to Run

1. Ensure all dependencies are installed.  
2. Run the application:

```bash
python connection.py
3. Follow the prompts to log in and select the functionality you want to test.
4. After completing a function, the menu will reappear so you can test other functionalities.
5. Select “Exit the program” to terminate the application.

## Notes

The application interacts with a SQL database; make sure your database connection details in connection.py are correct.

All user inputs are validated to prevent errors.

## Example Usage
Welcome! Please log in:
Username: user1
Password: ****
1. Search Business
2. Search User
3. Make Friend
4. Write Review
5. Exit the program
Select an option: 1
