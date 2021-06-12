from tkinter import *
from PIL import ImageTk,Image
import sqlite3


root = Tk()
root.title('Contact Book')
root.geometry("325x500")

# Databases

# Connecting to the database
conn = sqlite3.connect('contact_book.db')

# Creating cursor
c = conn.cursor()


# Creating Update function to update a record
def update():
	# Creating a database or connect to one
	conn = sqlite3.connect('contact_book.db')
	# Creating cursor
	c = conn.cursor()

	record_id = delete_box.get()

	c.execute("""UPDATE contacts SET
		first_name = :first,
		last_name = :last,
		address = :address,
		city = :city,
		state = :state,
		phone = :phone 

		WHERE oid = :oid""",
		{
		'first': f_name_editor.get(),
		'last': l_name_editor.get(),
		'address': address_editor.get(),
		'city': city_editor.get(),
		'state': state_editor.get(),
		'phone': phone_editor.get(),
		'oid': record_id
		})


	# Commiting Changes
	conn.commit()

	# Closing Connection 
	conn.close()

	editor.destroy()
	root.deiconify()

# Creating Edit function to update a record
def edit():
	root.withdraw()
	global editor
	editor = Tk()
	editor.title('Update A Record')
	editor.geometry("400x300")
	# Creating a database or connect to one
	conn = sqlite3.connect('contact_book.db')
	# Creating cursor
	c = conn.cursor()

	record_id = delete_box.get()
	# Query the database
	c.execute("SELECT * FROM contacts WHERE oid = " + record_id)
	records = c.fetchall()
	
	#Creating Global Variables for text box names
	global f_name_editor
	global l_name_editor
	global address_editor
	global city_editor
	global state_editor
	global phone_editor

	# Creating Text Boxes
	f_name_editor = Entry(editor, width=30)
	f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
	l_name_editor = Entry(editor, width=30)
	l_name_editor.grid(row=1, column=1)
	address_editor = Entry(editor, width=30)
	address_editor.grid(row=2, column=1)
	city_editor = Entry(editor, width=30)
	city_editor.grid(row=3, column=1)
	state_editor = Entry(editor, width=30)
	state_editor.grid(row=4, column=1)
	phone_editor = Entry(editor, width=30)
	phone_editor.grid(row=5, column=1)
	
	# Creating Text Box Labels
	f_name_label = Label(editor, text="First Name")
	f_name_label.grid(row=0, column=0, pady=(10, 0))
	l_name_label = Label(editor, text="Last Name")
	l_name_label.grid(row=1, column=0)
	address_label = Label(editor, text="Address")
	address_label.grid(row=2, column=0)
	city_label = Label(editor, text="City")
	city_label.grid(row=3, column=0)
	state_label = Label(editor, text="State")
	state_label.grid(row=4, column=0)
	phone_label = Label(editor, text="phone")
	phone_label.grid(row=5, column=0)

	# Looping through the records
	for record in records:
		f_name_editor.insert(0, record[0])
		l_name_editor.insert(0, record[1])
		address_editor.insert(0, record[2])
		city_editor.insert(0, record[3])
		state_editor.insert(0, record[4])
		phone_editor.insert(0, record[5])

	
	# Creating a Save Button To Save edited record
	edit_btn = Button(editor, text="Save Record", command=update)
	edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

	


# Creating Function to Delete A Record
def delete():
	# Creating a database or connect to one
	conn = sqlite3.connect('contact_book.db')
	# Creating cursor
	c = conn.cursor()

	# Deleting record
	c.execute("DELETE from contacts WHERE oid = " + delete_box.get())

	delete_box.delete(0, END)

	# Commiting Changes
	conn.commit()

	# Closing Connection 
	conn.close()



# Creating Submit Function For database
def submit():
	# Creating a database or connect to one
	conn = sqlite3.connect('contact_book.db')
	# Creating cursor
	c = conn.cursor()

	# Inserting into Table
	c.execute("INSERT INTO contacts VALUES (:f_name, :l_name, :address, :city, :state, :phone)",
			{
				'f_name': f_name.get(),
				'l_name': l_name.get(),
				'address': address.get(),
				'city': city.get(),
				'state': state.get(),
				'phone': phone.get()
			})


	# Commiting Changes
	conn.commit()

	# Closing Connection 
	conn.close()

	# Clearing The Text Boxes
	f_name.delete(0, END)
	l_name.delete(0, END)
	address.delete(0, END)
	city.delete(0, END)
	state.delete(0, END)
	phone.delete(0, END)

# Creating Query Function
def query():
	# Creating a database or connect to one
	conn = sqlite3.connect('contact_book.db')
	# Creating cursor
	c = conn.cursor()

	# Query the database
	c.execute("SELECT *, oid FROM contacts")
	records = c.fetchall()
	# print(records)

	# Looping through the records
	print_records = ''
	for record in records:
		print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" +str(record[6]) + "\n"

	query_label = Label(root, text=print_records)
	query_label.grid(row=12, column=0, columnspan=2)

	# Commiting Changes
	conn.commit()

	# Closing Connection 
	conn.close()


# Creating Text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
phone = Entry(root, width=30)
phone.grid(row=5, column=1)
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)


# Creating Text Box Labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State")
state_label.grid(row=4, column=0)
phone_label = Label(root, text="phone")
phone_label.grid(row=5, column=0)
delete_box_label = Label(root, text="Select ID")
delete_box_label.grid(row=9, column=0, pady=5)

# Creating Submit Button
submit_btn = Button(root, text="Add To Contact", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Creating a Query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=105)

#Creating A Delete Button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=105)

# Creating an Update Button
edit_btn = Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=112)


# Commiting Changes
conn.commit()

# Closing Connection 
conn.close()

root.mainloop()
