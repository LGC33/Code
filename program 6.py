
#Author :Larry Grace    due :March 26, 2017
#Assignment: program 6
#Header Attendance Data File Generator
#Explain they can create Single data file or a Multi data file
#Assign the value of 1 for a single data file
#Assign the value of 2 for a multi data file
# Assign the value of Q to quit the program
#Tell them they must choose (1,2,Q) if they select invaild input
#Ask them to enter a csv file name if valid input continue if in valid input tell them to please try again
#Ask them what class they want exported if valid input continue if invalid input tell them they must choose a valid class

import csv
import datetime
import json
import webbrowser

MENU = """1. Read an attendance csv file and create a single class output. ( data.js)
2. Read an attendance csv file and create a multiple class aggregate output (multidata.js)
Q. Quit"""
Class = "Enter the class you want exported to data.js"

def intial_choice():
    """ First intial choice  """
    while True:
        choice = input(MENU).upper().strip()
        if choice in ["1"]:
            return "1"
        if choice in ["2"]:
            return "2"
        if choice in ["Q"]:
            return "Q"
        print("You must enter 1,2, or Q")

def open_file():
    """ Opens the csv file. """
    
    while True:

        try:
            user_file = input("Enter the csv file name ==>")
            fh = open(user_file)
            return fh
            print(fh) 
        except FileNotFoundError:
            print("Could not open the file you supplied.  Please re-enter the name ")
        except IOError:
            print("There was an IO Error.  Please choose another file or fix the issue")
        except ValueError:
            print("There was an ValueError. PLease input proper name")

def class_list(passing):
    """Changes class to a class list"""
    class_list = []
    class_list2 = {}
    fh_csv = csv.reader(passing)
    for line in fh_csv:
        class_list.append(line)
        three =line[0],line[1],line[5]
    return class_list
    c1 = json.dumps(class_list)
    class_list2 = c1
def class_choice(cls):
    """ ask what class they want attendance for """
    
    while True:
        try:
            user_file = input("Enter the class you want exported to data.js ==)").upper()
            var_title = user_file
            for class_type in cls:
                if class_type[0] == user_file:
                    return user_file
                print("not here")
                    
        except FileNotFoundError:
            print("Could not open the file you supplied.  Please re-enter the name ")
        except IOError:
            print("There was an IO Error.  Please choose another file or fix the issue")
        except ValueError:
            print("There was an ValueError. PLease input proper name")
    
def class_date(lst):
    """docstring"""
    dates= []
    datetimes = []
    dd ={}
    for date in dates:
        date_convert = datetime.datetime.strptime(date, "%m/%d/%Y")
        datetimes.append(date_convert)
        for num in range(0,len(class_list)):
            if class_list[num][1] == date:
                date.sorted()
                return date
            dd = dates
    
            
        
          

Attendance = True
while  Attendance == True:
    print("""Attendance Data File Generator""")
    

    intial= intial_choice()
    
 
    if intial == "Q":
        print("You have chosen not to run the program")
        Attendance = False
    if intial == "1":
        Attendance = True
        file = open_file()
        cls = class_list(file)
        choice = class_choice(cls)
        dates= class_date('lst')
        var_title = choice
        
        webbrowser.open("ClassAttendance.html")
    if intial == "2":
         Attendance = True
         file = open_file()

 
