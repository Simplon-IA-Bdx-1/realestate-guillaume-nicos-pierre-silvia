import os
import mysql.connector
from dotenv import load_dotenv
from annonce import Annonce



def connectToDatabase():
    load_dotenv()
    return mysql.connector.connect(
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        database=os.getenv("MYSQL_DATABASE")
    )

def disconnectDatabase(cnx):
    cnx.close()

def createCursor(cnx):
    return cnx.cursor(dictionary=True)

def closeCursor(cursor):    
    cursor.close()

def findQuery(id):
    return ("SELECT * FROM annonces WHERE id = {} LIMIT 1".format(id))

def findAllQuery():
    return ("SELECT * FROM annonces")

#idannonce,typedetransaction,position,codepostal,codeinsee,ville,etage,idtypechauffage,idtypecuisine,naturebien,si_balcon,nb_chambres,nb_pieces,si_sdbain,si_sdEau,nb_photos,prix,surface,dpeL,dpeC

def get_all_annonces(cnx):
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


def insert_annonce(cnx, annonce):
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
