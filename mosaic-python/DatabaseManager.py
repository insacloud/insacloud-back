import sqlite3
import logging
import os


class SqliteManager:
    
    """
    Import pictures taken by users.
    The database will be filled with entries like :
        "rgb color in hex format" : "directory where a picture with this average color can be found"
    eg. "33CC66" : "folder1"

    For now, the color code will be only one byte ("80"), from "00" to "FF"
    as we'll work with black&white pictures only
    """

    def __init__(self, database):
        self.connection = sqlite3.connect(database)

    def close_connection(self):
        self.connection.close()

    def create_event(self, event_name):
        cursor = self.connection.cursor()
        cursor.execute('CREATE TABLE ' + event_name + ' (color text, path text)')  # ohh la belle injection des familles
        self.connection.commit()

    '''
    @eventName is the name of the event where the picture was taken. It's a table name in the database
    @raw is a list ('color', 'path')
    '''
    def insert_picture(self, event_name, row):
        # Check picture file and place it to the correct directory
        
        # Insert picture into database
        cursor = self.connection.cursor()
        logging.info("Row for insertion : ")
        logging.info(row)
        cursor.execute('INSERT INTO ' + event_name + ' VALUES (?,?)', row)
        self.connection.commit()
        logging.info('New picture inserted (color = ' + row[0] + ', path = ' + row[1] + ')')


