import db_utils as db

#
# Creaete connectiong and connect to an existing database using database name
# params: database name
#
#connection = db.connect_db(database='mydatabase')

#
# Create connection
#
connection = db.connect_db()


#
# Create new database
# params: connection object, database name
#
db.create_new_db(connection, 'mydatabase')
connection = db.connect_db(database='mydatabase')

#
# Delete database
# params: connection object, database name
#
#db.delete_db(connection, 'mydatabase')


#
# Create new table
# params: connection object, table name
#
db.create_new_table(connection, 'users')


#
# Insert new row into table
# params: connection object, table name, row dictionary
#  {'email': 'webmaster@python.org', 'password': 'very-secret'}
row = {'email': 'webmaster@python.org', 'password': 'very-secret'}
db.insert_query(connection, 'users', row)

#
# Search row in table
# params: connection object, table name
#
db.search_email_query(connection, 'users', 'webmaster@python.org')

#
# Close Connection
# params: connection object
#
db.close_connection(connection)