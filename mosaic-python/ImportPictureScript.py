import DatabaseManager, logging

databaseName = "events.db"
event1 = "Concert_Mika_2012"

dbMan = DatabaseManager.SqliteManager(databaseName)

dbMan.CreateEvent(event1)

dbMan.InsertPicture(event1, ["80", "Mika1.jpg"])




