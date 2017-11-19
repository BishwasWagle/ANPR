import pymysql as sq
from datetime import datetime
now = datetime.now()
now.strftime('%m/%d/%Y')


def store(id,image,data):

    db = sq.connect("127.0.0.1","root","","anpr" )

    cursor = db.cursor()
    

    sql = "INSERT INTO numberplate(id,number,image,date)VALUES ('%d', '%s', '%s', '%s' )" %(id, image, data,now)
    
    try:

        cursor.execute(sql)
    
        print "Done"

        db.commit()
    except:

        db.rollback()
        print "Not done"

    db.close()
    return
def fetch_data():
    db1 = sq.connect("127.0.0.1","root","","japan" )
    cursor = db1.cursor ()
# execute the SQL query using execute() method.
    cursor.execute ("select name,phone from visa")
# fetch all of the rows from the query
    data = cursor.fetchall ()
# print the rows
    for row in data :
         print row[0], row[1]
         print data[1]
# close the cursor object
    cursor.close ()
# close the connection
    db1.close ()
    return
# exit the program
    
    
image1="lu2245"
id=788
data="sandip"    
#store(id,image1,data) 
