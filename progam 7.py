#Author: Larry Grace Due: April 26th, 2017
#Assignment: Program 7
#
#
#
#
#
#
#


import csv
import random
import copy

MENU = """1. Play against AI
Q. Quit
"""


def intial_choice():
    """ First intial choice  """
    while True:
        choice = input(MENU).upper().strip()
        if choice in ["1"]:
            return "1"
        if choice in ["Q"]:
            return "Q"
        print("You must enter 1 or Q")
def pymon_choice(pyke_list):
    """ Pymon choice  """
    while True:
        try:
            for idx, item in enumerate(h):
                print ("{}. {}".format(idx,item))
            choice = input("please choose 0,1,or 2").upper().strip()
            if choice == ("0"):
                return pyke_list[0]
            if choice ==("1"):
                return pyke_list[1]
            if choice ==("2"):
                return pyke_list[2]
            print("You must enter 0,1, or 2,")
            if len(h) == 0:
                print("you lose")
                return False
        except IndexError:
            print("you must choose out of your hand")

def pymon_choice2(cpu):
    """ Pymon choice  """
    try:
        choice = random.randint(0,len(cpu)-1)
        return cpu[choice]
        if len(cpu)==0:
            print("you win")
    except ValueError:
        print("AI has no more pykemon")
def open_file():
    try:
        user_file = "pykemonindex.csv"
        fh = open(user_file)
        return fh
         
    except FileNotFoundError:
         print("Could not open the file you supplied.  Please re-enter the name ")
    except IOError:
         print("There was an IO Error.  Please choose another file or fix the issue")
    except ValueError:
         print("There was an ValueError. PLease input proper name")
def pyke_list(creatures):
    """Changes class to a class list"""
    pyke_list = []
    
    fh_csv = csv.reader(creatures)
    for line in fh_csv:
        pyke_list.append(line)
    return pyke_list
class creature(object):
    def __init__(self,name,hp,damage_delt, attack_type,weakness):
        self.name = name
        self.hp = hp
        self.damage_delt = damage_delt
        self.attack_type = attack_type
        self.weakness = weakness
    def __str__(self):
        return "{:<10} ({}) -{}".format(self.name,self.hp,self.attack_type,self.weakness)
    def __repr__(self):
        return self.__str__()
    def attack(self,cpu):
        results= random.randint(1,self.damage_delt)
        if self.attack_type == cpu.weakness:
           results = results*2
        results2 = cpu.hp -results
        cpu.hp = results2
        return "{:<10} ({}) -{} {} {} {} {} {} {}".format(self.name,self.hp,"does ",results,"of",self.attack_type,"damage to",cpu.name,results2)
    def is_alive(self):
        if self.hp <= 0:
            print(self,"is defeated")
            return False
        if self.hp > 0:
            return True

    
def choose(pyke_list):
    """ choose the cerature"""
    chose_list =[]
    for line in range (0,3):
        a = random.randint(0,len(pyke_list) - 1)
        chose_list.append( pyke_list[a])
    return chose_list        
                       
                       
def transform(choose):
    """stuff"""
    change = []
    for line in choose:
        monster = creature(line[0],int(line[1]),int(line[2]),line[3],line[4])
        change.append(monster)
    return change


def to_the_death(user,cpu):
    """battle to the death"""
    try:
        while user.is_alive()  and cpu.is_alive():
                results= user.attack(cpu)
                print(results)
                results2 = cpu.attack(user)
                print(results2)
    except AttributeError:
            print("you win")

        
    


        


Pymon_game = True
while  Pymon_game== True:
    print("""Pymon Creature Game""")
    

    intial= intial_choice()
    if intial == "Q":
        print("You have chosen not to run the program")
        Pymon_game = False
        break
    if intial == "1":
        Pymon_game = True
        print ("Let's Begin")
    file = open_file()
    p_lst = pyke_list(file)
    cpu = copy.deepcopy(p_lst)
    l =choose(p_lst)
    cpu2 = choose(p_lst)
    h = transform(l)
    cpu3 = transform(cpu2)
    pymon_pick = pymon_choice(h)
    cpu4 = pymon_choice2(cpu3)
    first_hit = random.randint(0,1)

    

    while len(h) or len(cpu3) > 0:
        if first_hit == 0 :
                print("user attacks first")
                user_1st = to_the_death(pymon_pick,cpu4)
                if pymon_pick.hp<=0:
                    h.remove(pymon_pick)
 #                   dp.append(pymon_pick)
                if len(h) == 0:
                    print("you lose")
                if cpu4.hp<=0:
                    cpu3.remove(cpu4)
 #                   cpu_dp.append(cpu4)
                if len(cpu3) == 0:
                    print("you lose")
                pymon_pick = pymon_choice(h)
                cpu4 = pymon_choice2(cpu3)
                if first_hit == 0 :
                    print("user attacks first")
                    user_1st = to_the_death(pymon_pick,cpu4)
                    if pymon_pick.hp<=0:
                        h.remove(pymon_pick)
 #                       dp.append(pymon_pick)
                    if cpu4.hp<=0:
                        cpu3.remove(cpu4)
 #                       cpu_dp.append(cpu4)
                    pymon_pick = pymon_choice(h)
                    cpu4 = pymon_choice2(cpu3)

        if first_hit == 1 :
                print("cpu attacks first")
                cpu_1st = to_the_death(cpu4,pymon_pick)
                if pymon_pick.hp<=0:
                    h.remove(pymon_pick)
  #                  dp.append(pymon_pick)
                if cpu4.hp<=0:
                    cpu3.remove(cpu4)
 #                   cpu_dp.append(cpu4)
                pymon_pick = pymon_choice(h)
                cpu4 = pymon_choice2(cpu3)
    break
