from PIL import Image
import logging


def process_image(image_path):
    try:
        picture = Image.open(image_path)
    except IOError:
        logging.info("Unable to open image " + image_path)
        raise IOError
    picture = _crop_image(picture)

    return picture

def _crop_image(image):
    im_width, im_height = image.size

    if im_width > im_height:
        image = image.crop((im_width/2-im_height/2), 0, (im_width/2+im_height/2), im_height)
    elif im_width < im_height:
        image = image.crop((im_height/2-im_width/2), 0, (im_height/2+im_width/2), im_width)
    else:
        pass

    return image

def _get_main_color(image):
    # For now, it uses the function from base-project

    r = 0
    g = 0
    b = 0
    count = 0
    pix = image.load()
    im_max_x, im_max_y = image.size

    for x in range(0, im_max_x):
        for y in range(0, im_max_y):s
            temp_r, temp_g, temp_b = pix[x,y]
            r += temp_r
            g += temp_g
            b += temp_b
            count += 1

     return float(r) / float(count), float(g) / float(count), float(b) / float(count)
