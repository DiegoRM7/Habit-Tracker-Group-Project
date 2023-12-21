# Change nothing in this file.
# Do not delete the comments
# Use the comments to help with trouble shooting
# Bool object not iterable? Read below, where do you find a bool/boolean?


# a cursor is the object we use to interact with the database
import pymysql.cursors
import platform


# this class will give us an instance of a connection to our database
class MySQLConnection:
    def __init__(self, db):
        # change the user and password as needed
        os_type = platform.system()
        # Set the password based on the operating system
        if os_type == "Windows":
            password = "root"
        if os_type == "Darwin":  # Assuming macOS
            password = "Lawrence8450$"

        connection = pymysql.connect (
            host="localhost",
            user="root",
            # trying show password based on OS
            password=(password),
            db=db,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True,
        )
        # establish the connection to the database
        self.connection = connection

    # the method to query the database
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)

                cursor.execute(query, data)
                if query.lower().find("insert") >= 0:
                    # INSERT queries will return the ID NUMBER of the row inserted
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                    result = cursor.fetchall()
                    return result
                else:
                    # UPDATE and DELETE queries will return nothing
                    self.connection.commit()
            except Exception as e:
                # if the query fails the method will return FALSE
                print("\n\n--------Something went wrong-----\n\n", e)
                return False
            finally:
                # close the connection
                self.connection.close()


# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)
