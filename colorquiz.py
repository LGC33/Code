########################################################################
##
## CS 101
## Program  : 3
## Name     : Larry Grace
## Email
##
## PROBLEM : Plays a quiz color game
##
## ALGORITHM : 
##
##        function play_again()
##            
##                while invalid_input
##                    choice = get upper case user choice of continueing.
##                        
##                        if choice == "Y" or choice == "YES"
##                                return True
##                        if choice == "N" or choice == "NO"
##                            return False
##                        Warn user of invalid input.
##
##        function get_number(prompt, min, max)
##
##                while invalid_input
##                        set value to number entered by user.  Display the prompt
##                        if value >= min and value <= max then
##                                return value
##                        Warn user about invalid input.
##
##        function get_color()
##            set color to random number 1 to 3
##                if color == 1 return "Red"
##                if color == 2 return "Green"
##                if color == 3 return "Blue"
##                        
##        function show_problem()
##            
##                text = get_color()
##                color = get_color()
##                set text on screen to value of text
##                set color of text on screen to color
##                set key to user key press
##                
##                if key == "r" and color == "Red" return True
##                if key == "b" and color == "Blue" return True
##                if key == "g" and color == "Green" return True
##                return False
##
##        function get_rating(time, correct)
##                if correct == 0 return "Poor"
##                rating = time / correct
##                if rating < 0.8 return "Great"
##                if rating < 1.0 return "Good"
##                return "Poor"
##                
##        function show_results(time, correct, total)
##                rating = get_rating(time, correct)
##                output the # of problems correct out of total and percentage
##                output the time it took them
##                output the rating they got.
##                
##        set running = True
##        while running == True
##
##                set number to get_number()
##
##                Create new Window
##                Create Text on window to click to begin
##                getMouse click from window
##                
##                for cnt = 5 to 0
##                        set text to cnt
##                        sleep 1 second
##                        
##                set start = current time
##                set correct = 0
##                
##                for problem = 1 to number 
##                    if show_problem()
##                            increment correct
##                
##                set end to current time
##                
##                set elapsedtime to end - start
##                show_results(elapsedtime, correct, number)
##                
##                set running = play_again()
## 
## ERROR HANDLING:
##      Number of problems cannot be less than 3 or greater than 20
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################


import graphics as gfx
import time
import random

MAIN_PROGRAM = """\t\tThe Flexible Mind

This game will keep your mind flexible.
* Choose the number of problems.
* A window will pop up with a countdown after the countdown the game begins
* A word in a given color will be displayed, Red, Green or Blue
   The text of the word will also be red, green or blue
   Enter the color of the word shown ( r - Red, g - Green, b - Blue ) not the word, but the color of the word
* After the game is over, you'll be shown how many you got right, the percentage and how long it took you.

"""

COLOR_CHOICES = ["Red", "Green", "Blue"]


def get_color(choice = COLOR_CHOICES):
    """ Returns a random color, "red green or blue" """
    value = random.randint(0, 2)
    return choice[value]

    
def get_number(prompt, min_value, max_value):
    """ Gets a number from the user """
    while True:

        result = int(input(prompt))
        if min_value <= result <= max_value:
            return result
        print("You must return a value between {} and {}".format(min_value, max_value))


def play_again():
    """ Asks the user if they want to play again.  Only accepts given values """
    while True:

        result = input("Do you want to play again? ==> ").upper()

        if result in ["Y", "YES"]:
            return True
        if result in ["N", "NO"]:
            return False
        print("You must enter Y/YES/N/NO")


def count_down(countdown_text):
    """ The argument is a Text Area in a window. In the center of the window it will display the countdown """
    for count in range(5, -1, -1):
        countdown_text.setText(count)
        time.sleep(1)


def is_answer_correct(answer, color):
    """ Returns true if the answer matches color.  R for Red, G for Green, B for Blue """
    if answer == "r" and color == "Red":
        return True
    if answer == "g" and color == "Green":
        return True
    if answer == "b" and color == "Blue":
        return True
    return False


def show_problem(win, text_area, number):
    """ Shows the problem and gets an answer from the user. """
    color = get_color(COLOR_CHOICES)
    text = "{}. {}".format(number, get_color(COLOR_CHOICES))

    text_area.setText(text)
    text_area.setOutline(color)

    answer = win.getKey()
    return is_answer_correct(answer, color)


def run_game(num_problems):
    """ Runs a game of color namer
    	Creates a GraphWin Window, does a countdown plays the game and then closes the window
    	
    """

    win = gfx.GraphWin("Flexible Mind Workout", 300, 300)
    text = gfx.Text(gfx.Point(150, 150), "Click to begin")
    text.draw(win)
    win.getMouse()

    # Do a countdown to the beginning of the game 
    count_down(text)

    correct = 0
    start_time = time.time()
    for problem in range(1, num_problems + 1):
        if show_problem(win, text, problem):
            correct += 1

    end_time = time.time()

    # Close the program at the end
    win.close()

    time_elapse = end_time - start_time
    if correct > 0:
        rate = time_elapse / correct
        if rate < 0.8:
            rating = "Great"
        elif rate < 1.0:
            rating = "Good"
        else:
            rating = "Poor"
    else:
        rating = "Poor"

    print()
    print("You got {} out of {} problems, or {:6.2%}".format(correct, num_problems, correct/num_problems))
    print("It took you {:6.2f} seconds".format(time_elapse))
    print("Your rating is {}".format(rating))
    print()
    

def main():
    """ Main loop of the program asks to keep running """

    running = True

    while running:

        print()
        print(MAIN_PROGRAM)
        print()

        problems = get_number("How many problems do you want? ==> ", 3, 20)
        run_game(problems)

        running = play_again()


main()
