import random
import csv
import copy


MAIN_MENU = """           Pymon Creature Game
1. Play against AI
Q. Quit Game
==> """
MAIN_CHOICES = ["1", "Q"]

DEAL_CARDS = 3


def load_creature(line):
    """ Returns a new instance of the creature. """
    name, hp, dmg, attack, weakness = line
    hp, dmg = int(hp), int(dmg)
    return Creature(name, hp, dmg, attack, weakness)


def load_creature_from_file(file):
    """ Returns a list of the creatures from the file """
    creatures = []
    
    fh = open(file)
    csv_fh = csv.reader(fh)
    for line in csv_fh:
        creature = load_creature(line)
        creatures.append(creature)

    fh.close()
    return creatures


def show_menu(menu, choices):
    """ Shows a menu and only returns if they give a valid choice """
    while True:
        user_choice = input(menu).upper()
        if user_choice in choices:
            return user_choice
        print("You must enter a valid choice of {}".format(",".join(choices)))
        

class Creature(object):
    def __init__(self, name, hp, dmg, attack_type, weakness):
        """ Create Creature """
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.attack_type = attack_type
        self.weakness = weakness

    def __str__(self):
        """ Returns String representation of the creature """
        return "{:<10} ({}) - {}".format(self.name, self.hp, self.attack_type[0])

    def __repr__(self):
        """ Returns string representation of the creature """
        return self.__str__()

    def attack(self, victim):
        """ attacks another creature """
        dmg_amount = self.dmg
        if victim.weakness == self.attack_type:
            dmg_amount = dmg_amount * 2
        dmg = random.randint(1, dmg_amount)
        victim.hp = victim.hp - dmg
        text = "{} does {} pt(s) of {} damage to {}".format(self, dmg, self.attack_type, victim)
        return text

    def copy(self):
        return copy.copy(self)

    def is_alive(self):
        return self.hp > 0

def random_creature(creature_list):
    """ Returns a randomly chosen creature """
    creature = random.choice(creature_list)
    return creature.copy()


def create_hand(creature_index, count):
    """ returns a hand of the given count of randomly selected creatures """
    hand = []
    for cnt in range(count):
        creature = random_creature(creature_index)
        hand.append(creature)
    return hand


def get_battle_card(player_hand):
    """ Asks the player for a battle hand """
    if len(player_hand) <= 1:
        return player_hand[0]

    choices = [str(cnt) for cnt in range(len(player_hand))]
    choice_prompt = "Please choose the first of 2 choices from your hand\n"
    choice_prompt += "\t\n".join(["{}. {}".format(index, str(creature)) for index, creature in enumerate(player_hand)])
    choice_prompt += "\n===> "
    choice = int(show_menu(choice_prompt, choices))
    return player_hand[choice]


def get_ai_battle_card(hand):
    """ returns 2 random cards from the computers hand """
    if len(hand) <= 1:
        return hand[0]
    hand_copy = hand[:]
    first = random.choice(hand_copy)
    return first    
        

def battle(player, ai):
    """ Does battle between player and AI.  Let's them choose cards. """
    player_bc = get_battle_card(player)
    ai_bc = get_ai_battle_card(ai)        

    if random.randint(0, 1) == 0:
        print("Player creature gets first hit")
        first_bc, second_bc = player_bc, ai_bc
        first_prompt, second_prompt = "(player)", "(ai)"
    else:
        print("AI creature gets first hit")
        first_bc, second_bc = ai_bc, player_bc
        first_prompt, second_prompt = "(ai)", "(player)"

    # Loop while the creatures are alive.
    while player_bc.is_alive() and ai_bc.is_alive():
        result = first_bc.attack(second_bc)
        print("{} {}".format(first_prompt, result))

        if second_bc.is_alive():
            result = second_bc.attack(first_bc)
            print("{} {}".format(second_prompt, result))
    if not player_bc.is_alive():
        player.remove(player_bc)
        print("Your {} was beaten by the ai {}\n".format(player_bc, ai_bc))
    if not ai_bc.is_alive():
        ai.remove(ai_bc)
        print("Your {} was victorious over the ai {}\n".format(player_bc, ai_bc))

def play_game(creature_index):
    """ Play a round of the game.  We'll do x cards and a choice of 2 each time. """
    player_hand = create_hand(creature_index, DEAL_CARDS)
    ai_hand = create_hand(creature_index, DEAL_CARDS)

    while len(player_hand) > 0 and len(ai_hand) > 0:
        battle(player_hand, ai_hand)            
        
    # Show winner
    if len(player_hand) > 0:
        print("You won!  Congrats ")
    else:
        print("The computer won!.  Try again and do better!")
    
lst = load_creature_from_file("pykemonindex.csv")
running = True
while running:

    choice = show_menu(MAIN_MENU, MAIN_CHOICES)
    if choice == "Q":
        running = False
    elif choice == "1":
        play_game(lst)
