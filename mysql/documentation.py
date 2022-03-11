from dc_mysql import db_connect, cursor_close, cursor_create, db_close

db = db_connect("server_address", "username", "password", "database_name") # Connects to database
c = cursor_create(db) # Initializes the cursor for the database

c.execute("SELECT * FROM table_name") # Sends an SQL command to the cursor, and executes it.
# If you want to change the database content, use db_variable_name (in this case 'db') .commit
# Example: 
# c.execute("INSERT INTO user_table (username, password) VALUES ('nikkie', 'Ch33s3McFuckDuck089!')")
# db.commit()
result = c.fetchall() # Gets all the rows from the SQL command

for row in result: # Loops through the data
    print(row) # Prints all every row of data

cursor_close(c) # Closes the database cursor
db_close(db) # Closes the database

############################
# MADE                     #
# BY                       #
# NikkieDev Software       #
# https://nikkiedev.com    #
############################