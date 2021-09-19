import db_utils as db
from bson.objectid import ObjectId


switcher = { 
        0: "Create Mongo Client", 
        1: "Create/Connect Database", 
        2: "Delete Database", 
        3: "Create/Connect Collection", 
        4: "Delete Collection",
        5: "Insert single Document",
        6: "Insert multiple Document",
        7: "Get First document",
        8: "Get Matched Document",
        9: "Get Document using ObjectID",
        10: "Find all Matched Documents",
        11: "Delete Document",
        12: "Close Connection",
        13: "Exit",
    } 

row = {'email': 'webmaster@python.org', 'password': 'very-secret'}

rowlist = [
  { "email": "Amy@python.org", "password": "Apple-st-652"},
  { "email": "Hannah@python.org", "password": "Mountain-21"},
  { "email": "Michael@python.org", "password": "very-secret"},
  { "email": "Sandy@python.org", "password": "Ocean-blvd-2"},
  { "email": "Betty@python.org", "password": "Green-Grass-1"},
  { "email": "Richard@python.org", "password": "very-secret"},
  { "email": "Susan@python.org", "password": "One-way-98"},
  { "email": "Vicky@python.org", "password": "Yellow-Garden-2"},
  { "email": "Ben@python.org", "password": "Park-Lane-38"},
  { "email": "William@python.org", "password": "Central-st-954"},
  { "email": "Chuck@python.org", "password": "Main-Road-989"},
  { "email": "Viola@python.org", "password": "Sideway-1633"}
]

client = None
database = None
collection = None

#
# Display all available options
#
def show_main_screen():
    print('\nPlease select from the following:\n')
    for key, val in enumerate(switcher):
        print(key, switcher[key])
    
    get_user_input()

#
# Handle user input option
#
def get_user_input():

    user_input = input("Select Option: ")
    
    try:
        user_input = int(user_input)
    except:
        user_input = 13
    
    
    global client
    global database
    global collection
    
    if user_input == 0:
        #
        # Create connection
        # params: host name, port number
        #
        client = db.connect_db(host_name='localhost', port_no=27017)
        get_user_input()
    
    elif user_input == 1:
        #
        # Create new database
        # params: connection object, database name
        #
        status, database = db.create_new_db(client, 'mydatabase')
        get_user_input()
        
    elif user_input == 2:
        #
        # Delete database
        # params: client object, database name
        #
        db.delete_db(client, 'mydatabase')
        get_user_input()
        
    elif user_input == 3:
        #
        # Create new collection
        # params: connection object, table name
        #
        status, collection = db.create_new_table(database, 'users')
        get_user_input()
        
    elif user_input == 4:
        #
        # Delete collection
        # params: collection object, database name
        #
        db.delete_collection(collection)
        get_user_input()
        
    elif user_input == 5:
        #
        # Insert new document into collection
        # params: connection object, table name, row dictionary
        #
        db.insert_query(collection, row)
        get_user_input()
        
    elif user_input == 6:
        #
        # Insert list of documents into collection
        # params: connection object, table name, row dictionary
        #
        db.insert_many_query(collection, rowlist)
        get_user_input()
        
    elif user_input == 7:         
        #
        # Get the first document from collection
        # params: connection object, query=None
        #
        db.find_one_query(collection)
        get_user_input()
        
    elif user_input == 8:
        #
        # Get single matching document in collection
        # params: connection object, query
        #
        db.find_one_query(collection, {"email": 'William@python.org'})
        get_user_input()
        
    elif user_input == 9:
        #
        # Search by document ObjectId
        # params: connection object, query
        #
        db.find_one_query(collection, {"_id": ObjectId('')})
        get_user_input()
        
    elif user_input == 10:
        #
        # Search multiple document in collection
        # params: connection object, query
        #
        db.find_many_query(collection, {"password": "very-secret"})
        get_user_input()
        
    elif user_input == 11:
        #
        # Delete document from collection
        # params: connection object, query
        #
        db.delete_query(collection, {"password": "very-secret"})
        get_user_input()
        
    elif user_input == 12:
        #
        # Close Connection
        # params: connection object
        #
        if client is not None:
            db.close_connection(client)
        get_user_input()
    
    elif user_input == 13:
        #
        # Close Connection and Exit Program
        # params: connection object
        #
        if client is not None:
            db.close_connection(client)
    
    else:
#        get_user_input()
        pass
    


show_main_screen()






