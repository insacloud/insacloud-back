import sqlite3
import logging
import ImageFormatter as imp


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
        self.__create_events_table()

    """
        Try to create the Events table in the database, used to record
        all different events for which we have or will have images.
    """
    def __create_events_table(self):
        cursor = self.connection.cursor()
        try:
            ''' could use sqlite_master and just look for the event name in the table names, but this way, we can add
                data to the events... '''
            cursor.execute('CREATE TABLE Events (id INTEGER PRIMARY KEY, name TEXT)')    # note : date might be added later
        except IOError:
            logging.info("'Events' table exists.")

    def close_connection(self):
        self.connection.close()

    """
        Check whether an event has already been registered in the base or not.
    """
    def has_event(self, event_name):
        cursor = self.connection.cursor()
        cursor.execute("Select * from Events where name="+event_name)
        ans = cursor.fetchone()
        if ans is not None:
            return True
        return False

    def create_event(self, event_name):
        cursor = self.connection.cursor()
        cursor.execute('CREATE TABLE ' + event_name + ' (color text, path text)')  # ohh la belle injection des familles
        self.connection.commit()

    '''
    @eventName is the name of the event where the picture was taken. It's a table name in the database
    @raw is a list ('color', 'path')
    '''
    def insert_picture(self, event_name, path):
        # Insert picture into database
        cursor = self.connection.cursor()
        logging.info("Row for insertion : ")
        logging.info(row)
        cursor.execute('INSERT INTO ' + event_name + ' VALUES (?,?)', row)
        self.connection.commit()
        logging.info('New picture inserted (color = ' + row[0] + ', path = ' + row[1] + ')')




class PostGreManager:
    # Later ?
    pass