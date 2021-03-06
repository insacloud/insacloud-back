import ImageFormatter as ImFormat
import DatabaseManager as Dbman
import logging


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

        The image folder tree should be something like (to be defined precisely later):
        --- img
            |- Concert_Mika             // name of the event, corresponding to a table name in the database
            |   |- Mosaic.jpg
            |   |- Big                      // big images (max 200 ko) that will be sent when user zoom
            |   |   |- img1.jpg             // the number after img is set by the DatabaseManager, it's the id returned
            |   |   |- img2.jpg
            |   |   |- ...
            |   |   |- img255.jpg
            |   |- Small                    // small images that will be used to create the mosaic
            |   |   |- img1.jpg             // the number after img is set by the DatabaseManager, it's the id returned
            |   |   |- img2.jpg
            |   |   |- ...
            |   |   |- img255.jpg
            |- Concert_Queen            // idem
            |   |- Mosaic.jpg
            |   |- Big
            |   |- Small
    """

    def __init__(self, database):
        self.sqlite_man = Dbman.SqliteManager()
        self.known_events_cache = []

    def add_resource(self, event_name, image_path):
        # Does event exist ?
        event_exist = self.__check_for_event(event_name)
        if not event_exist:
            try:
                self.sqlite_man.create_event(event_name)
            except Exception as e:
                logging.error("Error raised when adding resource image")
                raise e

        # Create image formatter and feed it with the image path
        im_format = ImFormat.ImageFormatter(image_path)
        main_colour = im_format.process_image(image_path)

        if not self.sqlite_man.has_event(event_name):
            self.sqlite_man.create_event(event_name)

    """
        Check whether or not the event to which caller wants to add a picture has already been registered in the base or
        not.
    """
    def __check_for_event(self, event_name):
        # Check for event in the local cache :
        for e in self.known_events_cache:
            if e == event_name:
                return True

        ans = self.sqlite_man.has_event(event_name)
        if ans: # update cache
            self.known_events_cache.append(event_name)
            return True

        return False



