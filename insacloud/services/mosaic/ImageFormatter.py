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

    def process_image(self, side):
        self.__crop_image()
        self.__resize_image(side,side)
        self.__black_and_white()
        return self.__get_main_color_black()


    def save_image(self, image_path):
        self.image.save(image_path)


    def get_image(self):
        return self.image

    """
        Crop input image so that you get a square image (no resize yet, only crop)
        NOT TESTED (and it should be)
    """
    def __crop_image(self):
        im_width, im_height = self.image.size

        hWidth = im_width / 2
        hHeight = im_height / 2

        minSide = im_width

        if im_width > im_height:
            minSide = im_height
        minSide = minSide / 2
        self.image = self.image.crop((int(hWidth - minSide), int(hHeight - minSide), int(hWidth + minSide), int(hHeight + minSide)))

    # I guess this will be used only at the beginning, then we should switch to colours.
    def __black_and_white(self):
        self.image = self.image.convert('L')


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


    def __get_main_color_black(self):
        # For now, it uses the function from base-project
        b = 0
        count = 0
        pix = self.image.load()
        im_max_x, im_max_y = self.image.size

        for x in range(0, im_max_x):
            for y in range(0, im_max_y):
                temp_b = pix[x,y]
                b += temp_b
                count += 1

        return float(b) / float(count)


    """
        resize input image so that it can be saved and then directly used in a mosaic if needed.
        Recommanded size 5x5px (not sure though) -> warning: we must also keep a good quality image, so that
        user can zoom in on the smartphone and get the bigger image.
    """
    def __resize_image(self, w, h):
        self.image = self.image.resize((int(w),int(h)), Image.ANTIALIAS)