import random

def validate_input():
    """ Asks for number of jobs until they provide a number > 0 """
    while True:
        jobs = int(input("How many job offers will you get? ==> "))
        if jobs > 0:
            return jobs
        print("Give me a valid number greater than 0")


# Main program loop.  Continues as long as they want
playing = True
while playing:

    print()
    print("Lets start the job offer simulator")

    # Get how many jobs they plan get offered
    print()
    how_many_jobs = validate_input()
    
    # Choose how many offers to refuse immediately
    print()
    choose_after = -1
    while choose_after < 0 or choose_after >= how_many_jobs:
        choose_after = int(input("How many offers should you reject? ==> "))
        if choose_after < 0:
            print("You must choose a number greater than or equal to zero.")
        if choose_after >= how_many_jobs:
            print("You must choose a number less than job offers you'll get")

    print()
    invalid_detail = True
    while invalid_detail:
        detail_choice = input("Do you want to see details of all offers?\nEnter 1 for details, 2 to skip details ==>")
        if detail_choice == "1":
            invalid_detail = False
            show_details = True
        elif detail_choice == "2":
            invalid_detail = False
            show_details = False
        else:
            print("You must choose either 1 or 2.  Please enter one of these values ")

    # Create and initialize variables for the loop of offers
    highest = 0
    offer_choice = 0
    highest_pre = 0
    # Loop through each offer and randomly get how many choices there are.
    for offer_number in range(1, how_many_jobs + 1):

        offer = random.gauss(65, 5)
        if highest < offer:
            highest = offer
        if offer_number <= choose_after:
            if show_details:
                print("Offer #", offer_number, " $", offer, " - Rejected")
            if highest_pre < offer:
                highest_pre  = offer
        if offer_number > choose_after:
            # If we haven't chosen one yet, then we need to choose this last one.
            if offer_choice == 0 and offer_number == how_many_jobs:
                offer_choice = offer
                if show_details:
                    print("Offer #", offer_number, " $", offer, " - Accepted")
            else:
                if offer_choice == 0 and offer > highest_pre:
                    if show_details:
                        print("Offer #", offer_number, " $", offer, " - Accepted")
                    offer_choice = offer
                else:
                    if show_details:
                        print("Offer #", offer_number, " $", offer, " - Rejected")

    print()
    print("Results")
    print("You chose the offer of $", offer_choice, "k")
    print("The highest offer was $", highest, "k")
    print("The highest offer before you could choose was ", highest_pre, "k")
    print("You lost out on $", highest - offer_choice, "k.") 

    # Ask the user if they want to continue or not.
    valid_input = False
    while not valid_input:

        user_choice = input("Do you want to try again? (Y/YES/N/NO) ==> ").upper()
        if user_choice in ["Y", "YES"]:
            valid_input = True
        elif user_choice in ["N", "NO"]:
            valid_input = True
            playing = False
        else:
            print("You must choose Y/YES/N/NO to continue")
            
