from libmysql import MYSQL

# pymysql.err.OperationalError: (2013, 'Lost connection to MySQL server during query')

def link():
    return MYSQL(
        dbhost="qdm164639440.my3w.com",
        dbuser="qdm164639440",
        dbpwd="lqc19980722",
        dbname="qdm164639440_db",
        dbcharset="utf8")


dbconn = link()



