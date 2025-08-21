#Author :Larry Grace    due :Feb 26, 2017
#Assignment: program 3
#Job offers
# Algorithm
#1.Display text as description of the game.
#2.Import grapics and create a window
#3.Provide text on the window
#4.Start a coutdown from 5
#5.Color of text and the name should be different, and\
#        with the color of the text, not the text it repersent.
#6.Add the correct user input as the score for the total.
#7.Generate the score at the end, tell how long it took by\
#           creating a start timr and subtract stop from start.
#8.If it takes them x amount of time and they had y amount of questions \
#     then it will generate a specific score represented as "poor, good, or great"
#9.Ask if they want to play again
#10.Only except vaild input and restart or end




import graphics as gfx
import time
import random
def get_number(prompt, min_value,max_value):
    """This function asks for input from the user and it is between min_value and max_value."""
    probs = int(input("Input number of problems you want ?==>"))
    while probs < min_value or probs > max_value:
          probs = int(input("Plase enter a number between 3 and 20.And how many problems do you want."))
    return probs
                    
def get_color():
    """Import random color as a string. Red, Green, Blue"""
    color= random.randrange(1,4)
    if color == 1:
        color_str ="Red"
    elif color == 2:
        color_str = "Green"
    else:
        color_str = "Blue"
    return color_str
def is_answer_correct(answer, color):
    """ Ask for correct input of the color"""
    if answer.upper() == color.upper() [0]:
    
        return True
    else:
        return False
def play_again():
    playing = True
    while playing == True:
        start = input("Do you want to try again")
        if start.upper() != "Y" or start.upper() != "YES" or start.upper() != "NO" or start.upper() != "N":
            start = input("Please input Y/YES to play agin or N/NO to end")
            if start.upper() == "Y" or start.upper() == "YES":
                return True
            elif start.upper() == "N" or start.upper()== "NO":
                return False
print("""This game will keep your mind flexible.
* Choose the number of problems you want.
* A window will pop up with a countdown after the countdown the game begins
* A word in a given color will be displayed, Red, Green or Blue
 The text of the word will also be red, green or blue
 Enter the color of the word shown ( R - Red, G - Green, B - Blue ) not the word, but the color of
the word
* After the game is over, you'll be shown how many you got right, the percentage and how long it took
you.""")

thinkingbot = True
while thinkingbot == True:


    g = get_number("Input the amount of problems you want",3,20)
    win = gfx.GraphWin("flexible mind", 300, 300)
    text = gfx.Text(gfx.Point(150, 150), "Click to begin")
    text.draw(win)
    win.getMouse()


    for cnt in range (5,0,-1):
        text.setText(cnt)
        time.sleep(1)
        

        results = 0
        start = time.time()

    for cnt in range(1,g+1,):
        allc = get_color()
        t_color =gfx.Text(gfx.Point(150, 150),"")
        t_color = text.setText(get_color())
        t_color = text.setOutline (allc)
        #t_color.draw(win)
        key = win.getKey()
        if is_answer_correct(key,allc)==True:
            results = results +1

    win.close()

    end = time.time()
    elasped = end- start

    if results == 0:
        print("Ohhhh you gotta quicker than that")
    elif elasped/results < 0.8:
        print(" Your the very best that no one ever was")
    elif elasped/results< 1:
        print(" You are not the fastest man alive")
    elif elasped/results >1:
        print("Welcome to the turtle club")

    print("You got",results,"out of", g, "problems")
    print("Your time was {:^5.2f} seconds to finish".format(elasped))
    thinkingbot = play_again()

    



