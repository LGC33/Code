#Author: Larry Grace Due: May 7, 2017
#Assignment Make up

MAIN_MENU = """           Speech Synonyms
1. Convert a Text file with synonyms
Q. Quit 
==> """
MAIN_CHOICES = ["1", "Q"]
def open_file(prompt):
    """ Returns a filehandle of a valid file that is open for reading. """
    
    while True:

        try:
            filename = input(prompt)
            fh = open(filename, "r", encoding="utf-8")
            return fh
        except FileNotFoundError:
            print("Could not open the file you supplied.  Please re-enter the name ")
        except IOError:
            print("There was an IO Error.  Please choose another file or fix the issue")
def open_list():
    """ Returns a filehandle of a valid file that is open for reading. """
    try:
        filename = open("synonyms_en.txt",encoding="utf-8")
        return filename
    except FileNotFoundError:
        print("Could not open the file you supplied.  Please re-enter the name ")
    except IOError:
        print("There was an IO Error.  Please choose another file or fix the issue")



def return_list_from_file(file_handle):
    """ returns a list of all the words file """
    list_of_list= []
    list_list =file_handle.readlines()
    for item in list_list:
        list_list2 = item.split(",")
        list_of_list.append(list_list2)
        for idx, item in enumerate(list_list2):
            item = item.strip()
            list_list2[idx] = item
        return list_list2

def show_menu(menu, choices):
    """ Shows a menu and only returns if they give a valid choice """
    while True:
        user_choice = input(menu).upper()
        if user_choice in choices:
            return user_choice
        print("You must enter a valid choice of {}".format(",".join(choices)))




synonyms = True
while synonyms:
       choice = show_menu(MAIN_MENU, MAIN_CHOICES)
       if choice == "Q":
            running = False
       elif choice == "1":
           text_file = open_file(prompt)
           words = return_list_from_file(file_handle)
           
