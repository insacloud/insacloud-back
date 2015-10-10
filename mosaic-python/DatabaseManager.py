import sqlite3, logging
from PIL import Image

class SqliteManager:

    '''
    Import pictures taken by users.
    The database will be filled with entries like :
        "rgb color in hex format" : "directory where a picture with this average color can be found"
    eg. "33CC66" : "folder1"

    For now, the color code will be only one byte ("80"), from "00" to "FF"
    as we'll work with black&white pictures only
    '''

    def __init__(self, database):
        self.connection = sqlite3.connect(database)

    def CloseConnection(self):
        self.connection.close()

    def CreateEvent(self, eventName):
        cursor = self.connection.cursor()
        cursor.execute('CREATE TABLE '+ eventName +' (color text, path text)') # ohh la belle injection des familles
        self.connection.commit()

    '''
    @eventName is the name of the event where the picture was taken. It's a table name in the database
    @raw is a list ('color', 'path')
    '''
    def InsertPicture(self, eventName, row):
        cursor = self.connection.cursor()
        logging.info("Row for insertion : ")
        logging.info(row)
        cursor.execute('INSERT INTO '+eventName+' VALUES (?,?)', row)
        self.connection.commit()
        logging.info('New picture inserted (color = ' + row[0] + ', path = ' + row[1] + ')')



