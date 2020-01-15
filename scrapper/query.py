def connectToDatabase():
    return mysql.connector.connect(
        user= MYSQL_USER,
        password=MYSQL_PASSWORD,
        host=MYSQL_HOST,
        database=MYSQL_DATABASE
    )