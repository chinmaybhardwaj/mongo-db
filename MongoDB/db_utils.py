from pymongo import MongoClient

    
# =============================================================================
# Connection helper functios
# =============================================================================

#
# Connect to the database
# params: database name
#
def connect_db(host_name=None, port_no=None):
    
    print('Checking Connection...')
    
    client = None
    status = False
    
    if host_name is not None:
        print('Connecting to host...')
        #
        # Connect to the database
        #
        try:
            
            #
            # You can also connect to a specific host & port using below code
            #
            client = MongoClient(host_name, port_no)
            #client = MongoClient('mongodb://localhost:27017/')
            # client = MongoClient()
            #
            status = True
            print('Connected to host....')
            
        except Exception as e:
            print('Error connecting to host. Error:\n', e)       
        
    else:
        #
        # Connect to localhost
        #
        client = MongoClient()
        print('Error connecting to', host_name) 
    
    
    return status, client

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
def create_new_db(client, db_name):

    status = False
    db = None
    
    if client is not None and db_name is not None and type(db_name) is str:        
        try:
            # Create a new Database
            # MongoDB creates databases and collections automatically for you
            # if they don't exist already.
            
            db = client[db_name]
     
            status = True
            print('Database', db_name, 'created successfully...')
                
        except Exception as e:
            print('Error creating new database.', db_name, '\n', e)
            
    else:
        print('Please check connection object or database name')
        
    return status, db


#
# Delete database
# params: connection object, database name
#
def delete_db(connection, db_name):
    
    status = False

    if connection is not None and db_name is not None and type(db_name) is str:        
        try:
           connection.drop_database(db_name)
            
           status = True
           print('Database:', db_name, 'deleted successfully...')
                
        except Exception as e:
            print('Error deleting database:', db_name, '\n', e)
            
    else:
        print('Please check connection object or database name')
        
    return status



# =============================================================================
# Table(Collection) helper functions
# =============================================================================
    
#
# Create new table(Collection)
# params: database object, table name
#
def create_new_table(database, table_name):

    status = False
    collection = None
    
    if database is not None and type(table_name) is str:        
        try:
            collection = database[table_name]
                
            status = True
            print('Collection:', table_name, 'created successfully...')
                
        except Exception as e:
            print('Error creating new collection:', table_name, '\n', e)
            
    else:
        print('Please check collection object or collection name')
    
    return status, collection


#
# Delete table(Collection)
# params: collection object, table name
#
def delete_collection(collection):
    
    status = False

    if collection is not None:        
        try:
            collection.drop()
            status = True
            print('Collection deleted successfully...')
                
        except Exception as e:
            print('Error deleting collection: \n', e)
            
    else:
        print('Please check connection object or collection name')
        
    return status

    
# =============================================================================
# CRUD (Create,Read,Update,Delete) operations
# =============================================================================

#
# Insert row(Document) into table(Collection)
# params: collection object, dict to be inserted
#
def insert_query(collection, row_dict):

    status = False
    
    if collection is not None:
        
        try:
            doc_id = collection.insert_one(row_dict)
            status = True
            print('Successfully inserted data.\nMongoId::\n', doc_id.inserted_id)
            
        except Exception as e:
            print('Error while inserting.\nError:\n', e)
        
    else:
        print('Please check collection object')
        
    return status


#
# Insert multiple rows(Documents) into table(Collection)
# params: collection object, list of dict to be inserted
#
def insert_many_query(collection, row_list):

    status = False
    
    if collection is not None:
        
        try:
            doc_id = collection.insert_many(row_list)
            status = True
            print('Successfully inserted data.\nMongoId::\n', doc_id.inserted_ids)
            
        except Exception as e:
            print('Error while inserting.\nError:\n', e)
        
    else:
        print('Please check collection object')
        
    return status


#
# Getting a single document from collection
# params: collection object, query
#    
def find_one_query(collection, query=None):

    status = False
    
    if collection is not None:
        
        if  query is not None:
            #
            # Returns a single document matching a query (or None if there are no matches).
            #
             try:
                result = collection.find_one(query)
                print(result)     
                status = True
                print('Matching document found.\nResult:\n', result)
        
             except Exception as e:
                print('Error while searching.\nError:\n', e)
        else:
            #
            # If query is None, get the first document from collection
            #
            try:
                result = collection.find_one()
                status = True
                print('First document of the collection:\nResult:\n', result)
            
            except Exception as e:
                print('Error while searching.\nError:\n', e)
           
    else:
        print('Please check connection object')
        
    return status   


#
# Getting multiple documents from collection
# params: collection object, query
#    
def find_many_query(collection, query):

    status = False
    
    if collection is not None:
        
        if  query is not None:
            #
            # Returns a single document matching a query (or None if there are no matches).
            #
             try:
                result = collection.find(query)
                status = True
                print('Matching document found.\nResult:\n')
                
                for mydoc in result:
                  print(mydoc)
        
             except Exception as e:
                print('Error while searching.\nError:\n', e)
        else:
            #
            # If query is None, get the first document from collection
            #
            try:
                result = collection.find({})
                status = True
                print('First document of the collection:\nResult:\n')
                for mydoc in result:
                  print(mydoc)
            except Exception as e:
                print('Error while searching.\nError:\n', e)
           
    else:
        print('Please check connection object')
        
    return status 

#
# Use any query 
# params: connection object, query
#    
def delete_query(collection, query):

    status = False
    
    if collection is not None:
        
        if  query is not None:
            #
            # Returns a single document matching a query (or None if there are no matches).
            #
             try:
                result = collection.delete_one(query)
                status = True
                print('Matching document found.\nResult:\n')
                
                for mydoc in result:
                  print(mydoc)
        
             except Exception as e:
                print('Error while searching.\nError:\n', e)
        else:
            #
            # If query is None, get the first document from collection
            #
            try:
                result = collection.find()
                status = True
                print('First document of the collection:\nResult:\n')
                for mydoc in result:
                  print(mydoc)
            except Exception as e:
                print('Error while searching.\nError:\n', e)
           
    else:
        print('Please check connection object')
        
    return status 