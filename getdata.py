from connection import mysql
class getDatas(object):
    def __init__(self):
        self.Connection = mysql.connect()
        self.Cursor = mysql.connect().cursor()
        
    def getAllData(self):
        self.Cursor.execute("SELECT * FROM tbl_user")
        aData = self.Cursor.fetchall()
        return aData
    
    def insertData(self,aData):
        usr_name = aData['usr_name']
        usr_email = aData['usr_email']
        usrType_id = aData['usrType_id']
        usr_password = aData['usr_password']
        
        self.cursor.execute("INSERT INTO tbl_usr(usr_name,usr_email,usrType_id,usr_password)) VALUES (%s,%s,%s,%s)",(
            usr_name,usr_email,usr_password,usrType_id
        ))
        
    def updateData(self,aData,usr_id):
        usr_name = aData['usr_name']
        usr_email = aData['usr_email']
        usrType_id = aData['usrType_id']
        usr_password = aData['usr_password']
        
        self.cursor.execute("UPDATE tbl_usr SET usr_name = '"+usr_name+"',usr_email='"+usr_email+"',usr_password='"+usr_password+"',usrType_id='"+usrType_id+"' WHERE usr_id="+str(usr_id)+"")
        
        
        self.Connection.commit()
        
        return self.Cursor.rowcount
