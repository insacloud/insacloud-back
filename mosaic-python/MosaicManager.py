import os
import ImageFormatter as ImFormat
import DatabaseManager as DBman


class MosaicManager:
    """
        Entry point for incoming images and outgoing images/mosaic
        - If an image arrives on the server, you call AddResource(event_name, image_path).
        MosaicManager will ask its ImageFormatter to open, crop and analyse image (color /
        saturation .. we'll see). Then it will aks its DatabaseManager to add the image to
        the event.db base, referencing all images for each event according to its main color
        (to be detailed later). If the image registration succed (image with exact same color
        value not already registered), the DatabaseManager returns the image id as he registered
        it and the MosaicManager will ask its ImageFormatter to save the image to the correct folder,
        with the id returned.
        - If you want the get the final mosaic for an event, you call GetMosaic

        The image folder tree should be :
        --- img
            |- Concert_Mika             // name of the event, corresponding to a table name in the database
            |   |- img1.jpg             // the number after img is set by the DatabaseManager, it's the id returned
            |   |- img2.jpg
            |   |- ...
            |   |- img255.jpg
            |- Concert_Queen            // idem
            |   |- img1.jpg
            |   |- ...
            |   |- img255.jpg

    """

    def __init__(self, database):
        self.sqliteMan = DBman.SqliteManager()

    def add_resource(self, event_name, image_path):
        im_format = ImFormat.ImageFormatter(image_path)
        im_format.process_image(image_path)

        if self.sqliteMan.has_event(event_name) == False:
            self.sqliteMan.create_event(event_name)

        pass

