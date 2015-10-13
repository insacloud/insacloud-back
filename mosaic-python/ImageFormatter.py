# add licence from base project ? or wait til we've modified everything :P ?

from PIL import Image
import logging


class ImageFormatter:

    def __init__(self, image_path):
        self.image_path = image_path
        try:
            self.image = Image.open(image_path)
        except IOError:
            logging.info("Unable to open image " + image_path)
            raise IOError

    def process_image(self):
        self.__crop_image(self.image)
        color = self.__get_main_color(self.image)

        return color

    def save_image(self, image_path):
        self.__resize_image() #fixed size for now maybe 5x5 px ?
        pass

    """
        Crop input image so that you get a square image (not resized yet, only croped)
    """
    def __crop_image(self):
        im_width, im_height = self.image.size

        if im_width > im_height:
            self.image = self.image.crop((im_width/2-im_height/2), 0, (im_width/2+im_height/2), im_height)
        elif im_width < im_height:
            self.image = self.image.crop((im_height/2-im_width/2), 0, (im_height/2+im_width/2), im_width)
        else:
            pass

    def __get_main_color(self):
        # For now, it uses the function from base-project
        r = 0
        g = 0
        b = 0
        count = 0
        pix = self.image.load()
        im_max_x, im_max_y = self.image.size

        for x in range(0, im_max_x):
            for y in range(0, im_max_y):
                temp_r, temp_g, temp_b = pix[x,y]
                r += temp_r
                g += temp_g
                b += temp_b
                count += 1

        return float(r) / float(count), float(g) / float(count), float(b) / float(count)

    """
        resize input image so that it can be saved and then directly used in a mosaic if needed.
        Recommanded size 5x5px (not sure though)
    """
    def __resize_image(self):
        pass