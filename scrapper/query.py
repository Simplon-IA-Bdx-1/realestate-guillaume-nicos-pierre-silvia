import os
import mysql.connector
from dotenv import load_dotenv
from annonce import Annonce


# Credentials are hidden into environment variables 
# for more security.
def connectToDatabase():
"""Connexion to the database.""" 
    load_dotenv()
    return mysql.connector.connect(
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        database=os.getenv("MYSQL_DATABASE")
    )

# Disconnection from the database
def disconnectDatabase(cnx):
"""Disconnection from the database."""
    cnx.close()

# The cursor is a buffering mechanism for browsing 
# rows of records in the result returned by a query.
def createCursor(cnx):
    return cnx.cursor(dictionary=True)

# Removal of the storage of the result of a query.
def closeCursor(cursor):    
    cursor.close()

# The function selects all the information stored
# in the database for the id you mention.
# Query which returns a dictionnary.
def findQuery(id):
    """Select information for a special ad."""
    return ("SELECT * FROM annonces WHERE id = {} LIMIT 1".format(id))

# The function selects all the information stored
# in the table "Annonces".
# Query which returns a dictionnary of dictionnary.
def findAllQuery():
    """Select information for all ads."""
    return ("SELECT * FROM annonces")

# The function gets all ads of our database.
# Returns a dictionnary.
def get_all_annonces(cnx):
    """Returns all ads on the database."""
    statement = findAllQuery()
    cursor = createCursor(cnx)
    cursor.execute(statement)
    results = cursor.fetchall()
    annonces = []
    if (cursor.rowcount == 0):
        annonces = None
    for result in results:
        # print(result)
        annonces.append(Annonce(**result))
    # print(annonces)
    closeCursor(cursor)
    return annonces

# The function insert an ad in our database.
# Each idannonce being unique, the function
# prevents any duplicate insertion.
def insert_annonce(cnx, annonce):
    """Insert an ad in the database - Not duplicated."""
    stmnt_list = []
    stmnt_list.append("INSERT INTO `{}` {}".format('annonces', annonce.get_fields_as_string()))
    stmnt_list.append("VALUES (" + ", ".join(["%s"] * len(annonce.get_fields())) + ")" )
    stmnt_list.append("ON DUPLICATE KEY UPDATE `id`=`id`")
    statement = "\n".join(stmnt_list)
    # print(statement)
    # print(annonce.get_values())
    cursor = createCursor(cnx)
    cursor.execute(statement, annonce.get_values())
    cnx.commit()
    closeCursor(cursor)


if __name__ == "__main__":

    cnx = connectToDatabase()
    annonce = Annonce(idannonce=12345, prix=1234)
    
    #insert_annonce(cnx, annonce)
    annonces = get_all_annonces(cnx)
    print(annonces)
