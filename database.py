import sqlite3

# Creating a database to store contacts
conn = sqlite3.connect('contact_book.db')

# Creating a cursor
c = conn.cursor()

c.execute("""CREATE TABLE contacts (
		first_name text,
		last_name text,
		address text,
		city text,
		state text,
		phone integer
		)""")

#Commiting Changes
conn.commit()

# Closing Connection 
conn.close()