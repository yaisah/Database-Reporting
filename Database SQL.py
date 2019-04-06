##Yaisah Granillo
#install the prettytable package
from prettytable import PrettyTable as pt
#this library will read the SQL database
import sqlite3

#this is the connection to the specified database
conn = sqlite3.connect('chinook.db')

#welcome message
print("Hello! Welcome to the Chinook Database.")
print("Below you will find a couple of options to help you display important information you have requested.")

#1 - employee titles
print("\nPossible Outputs:")
print("It is important to keep track of our employee titles for bonuses!")
print("Enter 1 to identify which employees are IT Staff.")

#cursor object to interact with the database to execute our operations
c = conn.cursor()
#this will execute the SQL Query for the first question
c.execute("SELECT FirstName, LastName, Title FROM employees WHERE Title = 'IT Staff'")
#this defines the headers of the expected result for the first question
col_names = [cn[0] for cn in c.description]
#this will fetch all our table rows of a query result set
rows = c.fetchall()

#you will see this style in all of the questions to display in prettytable format
#otherwise, it will print very offset
#you can see from the code, that we are expecting 3 columns to print

#defining  prettytable styles
y1 = pt()
#this is desired padding width for our table
y1.padding_width = 1
#this will add all columns into one table format, otherwise the columns are individual with no style
y1.add_column(col_names[0],[row[0] for row in rows])
y1.add_column(col_names[1],[row[1] for row in rows])
y1.add_column(col_names[2],[format(row[2]) for row in rows])
#aligns our second column to the left 
y1.align[col_names[1]]="l"
#aligns our third colum to the right
y1.align[col_names[2]]="r"

#2 - customers from USA and Canada 
print("\nMost of our customers are from USA and Canada")
print("Enter 2 to display a list of customers that are from these two countries.")
d = conn.cursor()
#display the first name, last name and country of our customers
d.execute("SELECT FirstName, LastName, Country FROM customers WHERE Country IN ('USA','Canada') ORDER BY Country")
col_names = [cn[0] for cn in d.description]
rows = d.fetchall()

y2 = pt()
y2.padding_width = 1
y2.add_column(col_names[0],[row[0] for row in rows])
y2.add_column(col_names[1],[row[1] for row in rows])
y2.add_column(col_names[2],[format(row[2]) for row in rows])
y2.align[col_names[1]]="l"
y2.align[col_names[2]]="r"

#3 - albums by artist
print("\nWe have a lot of available albums by Led Zeppelin")
print("Enter 3 to find out which albums are available by the band Led Zeppelin.")
e = conn.cursor()

#to display only the title of the specific artist with this query
e.execute("SELECT Title FROM albums WHERE ArtistId = 22")
col_names = [cn[0] for cn in e.description]
rows = e.fetchall()

y3 = pt()
y3.padding_width = 1
y3.add_column(col_names[0],[row[0] for row in rows])


#4 - audio file types
print("\nAudio files vary in quality.")
print("Enter 4 to view a variety of Media Types we have available.")
f = conn.cursor()
#with this query we will only display the name of the media type 
f.execute("SELECT Name FROM media_types")
col_names = [cn[0] for cn in f.description]
rows = f.fetchall()

y4 = pt()
y4.padding_width = 1
y4.add_column(col_names[0],[row[0] for row in rows])


#exit
print("\nEnter q to exit.")

#created this def function to loop the code in case the business users are interested in any additional questions without restarting the program

def output():

    action = input('What output would you like to see (1, 2, 3, 4, or q)?')
    #employee titles
    if action == '1':
        print("\nEmployees that are IT Staff.")
        print(y1)
        return output()
    #customers from USA and Canada 
    elif action == '2':
        print("\nCustomers that are from the USA and Canada.")
        print(y2)
        return output()
    #albums by artist
    elif action == '3':
        print("\nAlbums available by the band Led Zeppelin.")
        print(y3)
        return output()
    #audio file types
    elif action == '4':
        print("\nMedia Types we have available.")
        print(y4)
        return output()
    #exit
    elif action == 'q':
        print("\nGoodbye")
        exit()
    #invalid output
    else:
        print("\nOops. You entered an invalid response. For other questions you may be interested in contact our staff and we will create another ouput option!")
        return output()


output()

#this will close the database file
conn.close()
