#Author :Larry Grace    due :March 26, 2017
#Assignment: program 5
#Algorithim 
#import graphics, os module, random time
#take old functions and put it in new progaram
# ask user to open ppm directory if directory not found ask user for corrct input
#check ppm images for header if not found warn user to use another directory
#open window and create an image to draw on the window.


import graphics as gfx
import time

def open_file():
    """Prompts to open a file"""
    for filenames in os.listdir(path):
        with open(ospath.join(path,filename))as myfile:
            file_type= myfile[0]
            width, height=myfile[1].split()

def get_dir():
    """ Ask what directory they want to use """
    a = True
    while a:
        b = input("Input a dir that contains ppm images:")
        if os.path.isdir(a) is True:
            a = False
            return b
        elif os.path.isdir(b) is False:
            print ("Wrong file not a ppm")

def in_dir(b):
    lst = os.listdrir(b)
    py = True
    if lst == []:
        print("No picture")
        return False
    for num in range(0,len(lst)):
        files = os.path.join(b, lst(num))
        lister = []
        fh = open(files)
        for line in fh:
            lister.append(line)
            fh.close()
            if lister[0].strip() != "P3":
                print ("Image must begin with P3")
                return False
                break
            if lister[1].strip() !="320 200":
                print ( "All images must be the same size ")
                return False
                break
            if lister[2]. strip() != "255":
                print (" images must have color depth of 255")
                return False




a = get_dir()
b = in_dir()
while b ==False:
    a = get_dir()
    b = indir(a)
    lst= os.listdir(a)

c = get_list(a)


win = gfx.Graphwin ("Slideshow",500,500)
img = gfx.Image(gfx.point(250,250),400,250)
img.draw(win)
for b3 in range (400):
    for a3 in range (250):
        img.setPixel(a3,b3, "red")

i= []
for num1 in range (0, len(c)):
    for num in range(0,len(c[num1])):
        for liste in c [num1][num]:
            p = []
            p.append(liste)
            i.append(p)

      
