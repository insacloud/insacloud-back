import DatabaseManager
import logging

databaseName = "events.db"
event1 = "Concert_Mika_2012"

dbMan = DatabaseManager.SqliteManager(databaseName)

dbMan.create_event(event1)

dbMan.insert_picture(event1, ["80", "Mika1.jpg"])




