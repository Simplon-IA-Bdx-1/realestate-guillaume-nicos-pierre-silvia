import os
import mysql.connector

def connectToDatabase():
    return mysql.connector.connect(
        user= MYSQL_USER,
        password=MYSQL_PASSWORD,
        host=MYSQL_HOST,
        database=MYSQL_DATABASE
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
def insertAnnonces(annonces):
    insert_stmt = (
        "INSERT INTO `annonces` (`idannonce`, `typedetransaction`, `position`, `codepostal`, `codeinsee`,`ville`, `etage`, `idtypechauffage`, `idtypecuisine`, `naturebien`,`si_balcon`, `nb_chambres`, `nb_pieces`, `si_sdbain`, `si_sdEau`, `nb_photos`, `prix`, `surface`, `dpeL`, `dpeC`)" 
        "VALUES ('{}', '{}', '{}', '{}', '{}','{}', '{}', '{}', '{}', '{}','{}', '{}', '{}', '{}', '{}','{}', '{}', '{}', '{}', '{}')"
        "ON DUPLICATE KEY UPDATE `id`=`id`"
    )
    data = (annonces.idannonce,annonces.typedetransaction,annonces.position,annonces.codepostal,annonces.codeinsee,annonces.ville,annonces.etage,annonces.idtypechauffage,annonces.idtypecuisine,annonces.naturebien,annonces.si_balcon,annonces.nb_chambres,annonces.nb_pieces,annonces.si_sdbain,annonces.si_sdEau,annonces.nb_photos,annonces.prix,annonces.surface,annonces.dpeL,annonces.dpeC)
    return (insert_stmt, data)