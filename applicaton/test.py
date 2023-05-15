import creds    # this holds the database credentials - it is excluded from the repository
import pymysql.cursors

def connectdb():
    """
    Convenience function to connect to the database
    TODO: Would I be better holding one connection open using Flask.g rather then one per page?
    """
    return pymysql.connect(host=creds.host, user=creds.user, password=creds.password, 
        database=creds.database, charset=creds.charset, cursorclass=pymysql.cursors.DictCursor)

# create connection
connection = connectdb()

# load user into database
with connection:
    with connection.cursor() as cursor:
        
        # create a new user
        sql = "INSERT INTO `users` (`town`, `park`) VALUES (%s, %s)"
        cursor.execute(sql, ("FAKE TOWN", "FAKE PARK"))