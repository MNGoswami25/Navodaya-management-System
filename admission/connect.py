import mysql.connector as cs
def connection():
    global con,cur
    con=cs.connect(host = "localhost",
                           user = "root",
                           passwd="1234",
                            database = "cs_project")
    cur = con.cursor()
    

if(connection()):
    print("Connected")
