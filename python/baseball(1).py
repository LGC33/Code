#

#


# while Running
import random

running = True
while running:

    print("Playing sim")
    home_score = visitor_score = 0
    inning = 1
    while inning < 10:
        print("Inning # ", inning)
        v_runs = random.randint(1, 4)
        h_runs = random.randint(1, 4)

        print("Visitors Got ", v_runs)
        print("Home got ", h_runs)

        home_score += h_runs
        visitor_score += v_runs
        
        inning = inning + 1

    # Summary
    print("Home ", home_score)
    print("Visitors ", visitor_score)

    choice = input("Continue ? Y")
    if choice.upper() != "Y":
        running = False
# initialize variables
# loop while playing
# Ask to continue
