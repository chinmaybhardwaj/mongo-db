import sqlite3

    
# =============================================================================
# Connection helper functios
# =============================================================================

#
# Connect to the database
# params: database name
#
def connect_db(database=None):
    
    print('Checking Connection...')
    
    connection = None
    db = database + '.db'
    
    if database is not None:
        print('Connecting to localhost...')
        #
        # Connect to the database
        #
        try:
            connection = sqlite3.connect(db)
            print('Connected to', db, '....')
            
        except Exception as e:
            print('Error connecting to ', db, '. Error:\n', e)       
        
    else:
        print('Please check database name')

    
    return connection

#
# Close connection after use
# params: connection object
#
def close_connection(connection):

    status = 'Failed to close connection.'

    print('Closing Connection...')
    
    if connection is not None:
        try:
            connection.close()
            status = 'Connection closed successfully.'
        except Exception as e:
            status = 'Error: {}'.format(e)
            
    else:
       status += ' Connection cannot be None.' 
        
    print(status)
    return status
        
# =============================================================================
# Database helper functions
# =============================================================================
   
#
# Create new database
# params: connection object, database name
#
def create_new_db(connection, db_name):

    status = False

    if connection is not None and db_name is not None and type(db_name) is str:        
        try:
            with connection.cursor() as cursor:
                # Create a new Database
                create_db_query = "CREATE DATABASE IF NOT EXISTS " + db_name
                cursor.execute(create_db_query)
          
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                connection.commit()
                
                status = True
                print('Database', db_name, 'created successfully...')
                
        except Exception as e:
            print('Error creating new database.', db_name, '\n', e)
            
    else:
        print('Please check connection object or database name')
        
    return status


#
# Delete database
# params: connection object, database name
#
def delete_db(connection, db_name):
    
    status = False

    if connection is not None and db_name is not None and type(db_name) is str:        
        try:
            with connection.cursor() as cursor:
                # Create a new Database
                delete_db_query = "DROP DATABASE IF EXISTS " + db_name
                cursor.execute(delete_db_query)
          
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                connection.commit()
                
                status = True
                print('Database:', db_name, 'deleted successfully...')
                
        except Exception as e:
            print('Error deleting database:', db_name, '\n', e)
            
    else:
        print('Please check connection object or database name')
        
    return status



# =============================================================================
# Table helper functions
# =============================================================================
    
#
# Create new table
# params: connection object, table name
#
def create_new_table(connection, table_name):

    status = False

    if connection is not None and type(table_name) is str:        
        try:
            with connection.cursor() as cursor:
                # Create a new Database
                create_table_query = "CREATE TABLE IF NOT EXISTS " + table_name + "(email CHAR(20) NOT NULL, password CHAR(20))"
                cursor.execute(create_table_query)
          
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                connection.commit()
                
                status = True
                print('Table:', table_name, 'created successfully...')
                
        except Exception as e:
            print('Error creating new table:', table_name, '\n', e)
            
    else:
        print('Please check connection object or table name')
    
    return status


#
# Delete table
# params: connection object, table name
#
def delete_table(connection, table_name):
    
    status = False

    if connection is not None and type(table_name) is str:        
        try:
            with connection.cursor() as cursor:
                # Create a new Database
                delete_table_query = "DROP TABLE IF EXISTS " + table_name
                cursor.execute(delete_table_query)
          
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                connection.commit()
                
                status = True
                print('Table:', table_name, 'deleted successfully...')
                
        except Exception as e:
            print('Error deleting table:', table_name, '\n', e)
            
    else:
        print('Please check connection object or table name')
        
    return status

    
# =============================================================================
# CRUD (Create,Read,Update,Delete) operations
# =============================================================================

#
# Insert row into table
# params: connection object, table name, dict to be inserted
#
def insert_query(connection, table_name, row_dict):

    status = False
    
    if connection is not None:
        
        try:
            with connection.cursor() as cursor:
                # Create a new record
                # Convert dictionary into sql query
                placeholders = ', '.join(['%s'] * len(row_dict))
                columns = ', '.join(row_dict.keys())
                sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % (table_name, columns, placeholders)
                cursor.execute(sql, list(row_dict.values()))
        
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()

            status = True
            print('Successfully inserted data.\nQuery:\n', sql)
            
        except Exception as e:
            print('Error while inserting.\nQuery:\n', sql, '\nError:\n', e)
        
    else:
        print('Please check connection object')
        
    return status
        
        
#
# Search for row in table
# params: connection object, query
#
def search_email_query(connection, table_name, email):

    status = False
    
    if connection is not None:
        try:
        
            with connection.cursor() as cursor:
                # Read a single record
#                sql = "SELECT `email`, `password` FROM `" + table_name + "` WHERE `email`=%s"
#                cursor.execute(sql, (email,))
                
                # Passing email directly is insecure
                # Do this instead
                txt = (email,)
                cursor.execute("SELECT `email`, `password` FROM `" + table_name + "` WHERE `email`=?", txt)

                result = cursor.fetchone()
                
                print(result)     
                status = True
                print('Successfully inserted data.\nQuery:\n', sql)
        
        except Exception as e:
            print('Error while inserting.\nQuery:\n', sql, '\nError:\n', e)
           
    else:
        print('Please check connection object')
        
    return status   
    

#
# Use any query 
# params: connection object, query
#    
def master_query(connection, query):

    status = False
    
    if connection is not None:
        try:
        
            with connection.cursor() as cursor:
                cursor.execute(query)

                status = True
                print('Successfully.\nQuery:\n', query)
        
        except Exception as e:
            print('Error.\nQuery:\n', query, '\nError:\n', e)       
        
    else:
        print('Please check connection object')
        
    return status   
        
      