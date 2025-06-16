########################################################################
##
## CS 101
## Program  : 5 - Slide Show
## Name     : 
## 
##
## PROBLEM : Read in several PPM files and do a slideshow from the directory
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

import Image
import graphics as gfx
import os
import time

def load_ppm_to_image(ppm_file):
    """ Loads the ppm file given as a list into an image
    :param ppm_file: list of strings of the lines from the file.
    :return: Image object from gfx Library
    """
    size = ppm_file[1].split(" ")
    width, height = int(size[0]), int(size[1])
    img = gfx.Image(gfx.Point(width // 2, height // 2), width, height)

    for y in range(height):
        for x in range(width):
            address = (y * width + x) * 3 + 3
            red, green, blue = int(ppm_file[address]), \
                               int(ppm_file[address + 1]), \
                               int(ppm_file[address + 2])
            img.setPixel(x, y, gfx.color_rgb(red, green, blue))
    return img


def load_file(file_name):
    """ Loads a file and returns a list of the lines of from the file.
    :param file_name: Name of file to open.
    :return: list - List of strings.  Each element is a line from the file.
    """
    file = open(file_name)
    data = file.read()
    file.close()
    return data.split("\n")


def get_directory(prompt):
    """ Asks the user for a valid directory until the user supplies one
    :param prompt: str - The string to display to the end user.
    :return: str - The string name of the valid directory the user finally gave.
    """

    while True:
        directory = input(prompt)
        if os.path.isdir(directory):
            return directory
        print("You did not supply a valid directory ")


def valid_images(images):
    """ Returns True if the images have the same size, a P3 header and proper bit depth
    :param images: list of lists.  Each element is a list of hte lines in all the files.
    :return: bool - True if the images are all valid, False if they are not.
    """
    if len(images) == 0:
        print("This directory does not contain any ppm files.  Please select another one ")
        return False

    is_valid = True
    # Check to make sure the images all have the correct P3 and 255 header
    for image in images:
        if image[0] != "P3":
            print("PPM images must begin with P3 in the header")
            return False
        if image[2] != "255":
            print("PPM Images must have a color depth of 255")
            return False

    # Check that all the images have the same size.
    size = images[0][1]
    for img in images[1:]:
        if img[1] != size:
            print("All images in the directory must have the same size ")
            return False
    return True


def load_ppm_images_into_list(directory):
    """ Returns a list of all the all the files in the directory.  Each element is a list
    :param directory: str : Name of directory.
    :return: Returns a list.  Each item in the list is a list of the contents from a ppm file in that directory.
    """
    image_list = []
    for file in os.listdir(directory):
        if file.upper().endswith(".PPM"):

            ppm_file = load_file(os.path.join(img_dir, file))
            image_list.append(ppm_file)
    return image_list


def create_img_panels(image_list):
    """ Reads the ppm image lists and returns a list of panels with the images loaded
    :param image_list: list - Thi sis  alist where each element is a list from the ppm file.
    :return: list of gfx.Image created from the ppm images.
    """
    panels = []

    for img in image_list:
            img_pnl = load_ppm_to_image(img)
            panels.append(img_pnl)

    return panels

# Loop until we are given a valid directory
invalid_dir = True
while invalid_dir:

    # Get Directory from user.
    img_dir = get_directory("\nInput a directory that contains ppm images => ")

    # Load the images.
    images = load_ppm_images_into_list(img_dir)

    # If they are valid images, then set token to false.
    if valid_images(images):
        invalid_dir = False

# Get size, then width and height of images.
size = images[0][1].split()
width, height = int(size[0]), int(size[1])

# Create a window of the perop width and height
win = gfx.GraphWin("SlideShow", width, height, autoflush=False)

# Create list of image panels with the images placed on them.
img_panels = create_img_panels(images)


img_num = 0
# While the window is open iterate through each panel, and show then unshow it.
while win.isOpen():

    img = img_panels[img_num]
    img.draw(win)
    win.redraw()
    
    img_num = (img_num + 1) % len(img_panels)
    time.sleep(2)
    img.undraw()
