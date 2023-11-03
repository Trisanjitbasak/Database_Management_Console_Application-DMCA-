# Import necessary libraries
import pandas as pd
import mysql.connector
import os

# Clear the console
os.system('cls')

# Establish a connection to the MySQL server
db = mysql.connector.connect(
    host = "localhost",
    port = "3306", 
    user = "root",
    passwd = "admin123",
)

# Create a cursor object
conn = db.cursor()

# Try to use the existing database, if it doesn't exist then create a new one
try:
    conn.execute("use Company_database;")
except:
    conn.execute("create database Company_Database")

# Print the options for the user
print("Enter 1 to see/modify employee table")
print("Enter 2 to see/modify branch table")
print("Enter any number to exit")

# Get the user's choice
a = int(input())

# Main loop
while True:
    fname=0
    if(a == 1):
        print("Enter 1 to see employee table")
        print("Enter 2 to modify employee table")
        print("Enter 3 to create table")
        print("Enter 4 to exit to main menu")
        b = int(input())
        if(b == 1):
            # Fetch and display the employee table
            conn.execute("select * from employee")
            data = conn.fetchall()
            table = pd.DataFrame(data, columns=['first_name', 'last_name', 'email_id', 'phone_number', 'Address', 'Company', 'salary'])
            print(table)
            db.commit()
        elif(b == 2):
            while True:
                print("Enter 1 to add employee")
                print("Enter 2 to remove employee")
                print("Enter 4 to exit to main menu")
                c = int(input())
                if(c == 1):
                    # Get the details of the new employee from the user
                    print("Enter the first_name")
                    fname = input()
                    print("Enter the last_name")
                    lname = input()
                    print("Enter the email_id")
                    email = input()
                    print("Enter the phone_number")
                    phno = input()
                    print("Enter the address")
                    add = input()
                    print("Enter the Company")
                    comp = input()
                    print("Enter the Salary")
                    sal = int(input())
                    # Insert the new employee into the database
                    conn.execute("""INSERT INTO EMPLOYEE VALUES(%s, %s, %s, %s, %s, %s, %s)""",(fname, lname, email, phno, add, comp, sal))
                    db.commit()
                    if(conn):
                        print("Data restored")
                    else:
                        print("error occurred")    
                elif(c == 2):
                    # Get the name of the employee to be removed from the user
                    fname1 = input("Enter the name of the employee to be removed: ")
                    # Remove the employee from the database
                    conn.execute("""DELETE FROM employee WHERE first_name=%s""",(fname1,))
                    db.commit()
                elif(c == 3):
                    break;    
        elif(b==3):
            try:
                # Try to create the employee table
                conn.execute(""" CREATE TABLE employee(
                        first_name VARCHAR(1000),
                        last_name VARCHAR(1000),
                        email VARCHAR(1000),
                        phone_number VARCHAR(1000),
                        address VARCHAR(1000),
                        company VARCHAR(1000),
                        salary int
                        );""")
                db.commit();
            except:
                print("table already exists");
        else:    
            break;        
    elif(a == 2):
        print("Enter 1 to see branch table")
        print("Enter 2 to modify branch table")
        print("Enter 3 to exit to main menu")
        d = int(input())
        if(d == 1):
            try:
                # Fetch and display the branch table
                conn.execute("select * from branch")
                data = conn.fetchall()
                table = pd.DataFrame(data, columns=['branch_code', 'district', 'city', 'state'])
                print(table)
                db.commit()
            except:
                print("No data to show");
        elif(d == 2):
            while True:
                print("Enter 1 to add branch")
                print("Enter 2 to remove branch")
                print("Enter 3 to create table")
                print("Enter 4 to exit to main menu");
                e = int(input())
                if(e == 1):
                    # Get the details of the new branch from the user
                    print("Enter the branch_code")
                    bcode = int(input())
                    print("Enter the district")
                    district = input()
                    print("Enter the city")
                    city = input()
                    print("Enter the state")
                    state = input()
                    # Insert the new branch into the database
                    conn.execute("""INSERT INTO BRANCH VALUES(%s, %s, %s, %s)""",(bcode, district, city, state))
                    db.commit()
                    if(conn):
                        print("Data restored")
                    else:
                        print("error occurred")    
                elif(e == 2):
                    # Get the branch code of the branch to be removed from the user
                    bcode1 = input("Enter the name of the branch_code of the branch to be removed")
                    # Remove the branch from the database
                    conn.execute("""DELETE FROM branch WHERE branch_code=%s""",(bcode1,))
                    db.commit()
                elif(e == 3):
                    try:
                        # Try to create the branch table
                        conn.execute("""CREATE TABLE branch(
                            branch_code INT,
                            district VARCHAR(1000),
                            city VARCHAR(1000),
                            state VARCHAR(1000)
                            );""")
                    except:
                        print("Table already exists");
                else:
                    break;

        elif(d == 3):
            break;
    else:
        break;        
# Close the cursor and the database connection
conn.close()
db.close()
