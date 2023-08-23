
import graphics as gfx
import random 
import time 
#functions depend on this value #win = gfx.GraphWin("Flexible Mind Game!" , 500, 500) 


#returns a random color of red blue or green
def get_color():
	"""returns a random color from the options red, green or blue""" 
	colors = ["Red", "Green", "Blue"]
	pick = random.randint(0,2)
	color_pick = colors[pick]
	return color_pick
	
	
# gets an input from user of r g or b, re
def get_color_input(): 
	"""Gets from the user 'r' 'g' or 'b' and returns the color picked""" 
	un_print_warning = False
	while True:
		entry = win.getKey()
		#unprints the warning message only if it has been put up
		if un_print_warning == True:
			warning_messsage.undraw()
		entry = entry.lower()
		#validates that the entry is good and returns the value
		if entry == "r"  or entry == "g"  or entry == "b":
			return entry
		#prints a warning message if entry is invalid
		warning_messsage = gfx.Text(gfx.Point(250,275), "sorry please enter 'r' 'b' or 'g'")
		warning_messsage.draw(win)
		un_print_warning = True


# gets the number of rounds the player wants to play
#validates that the entry is a number between 3 and 20
def get_number(prompt , min_value , max_value):
	'''displays prompt and returns numeric value if it falls between min and max'''
	while True:
		#prints prompt for user	
		message = gfx.Text(gfx.Point(250,200), prompt)
		message.draw(win)
		
		#initializes values
		enter_key_pressed = False
		user_entry = ""
		entry_printer = gfx.Text(gfx.Point(250,250), "")
		
		
		
		while enter_key_pressed == False: 
			#gets and input key from user
			entry = win.getKey()
			entry_printer.undraw()
			
			# concatenate the value into string if the key is digit
			if entry.isdigit():
				user_entry = user_entry + entry
				
			# allows user to backspace while entering the number of games 
			if entry == "BackSpace":
				# avoids passing empty string to int() 
				if user_entry != "":
					# if value of user entry is greater than 2 digits removes last digit
					if int(user_entry) > 9:
						user_entry = str(int(user_entry)//10)
					# if value of user entry is one digit returns empty string
					else:
						user_entry = ""
				
			# prints the entry so the user can see their entry
			entry_printer = gfx.Text(gfx.Point(250,250), user_entry)
			entry_printer.draw(win)
			
			# ends the entry process
			if entry == "Return":
				enter_key_pressed = True
	
		#waits for enter key from user to send number for validation
		if enter_key_pressed:
			if user_entry.isdigit(): 
				
				user_entry = int(user_entry)
				if user_entry >= min_value and user_entry <= max_value:
					message.undraw()
					entry_printer.undraw()
					
					return user_entry
			
		# if the entry is invalid 		
		entry_printer.undraw()
		message.undraw()		
		error_message = gfx.Text(gfx.Point(250,200), "Sorry! Invalid entry...")
		error_message.draw(win)
		time.sleep(1.5)
		error_message.undraw()
		

#This screen displays the rules and waits for the user to click
def rules_wait():
	''' Prints rules and waits for click to start game ''' 
	#prints rules and an example of the rules
	message = gfx.Text(gfx.Point(250,175), "Rules:\n\nWhen a word appears, enter the color of the word\nnot the word itself. For instance, if you see:")
	message.draw(win)
	
	#creates example for user
	example = gfx.Text(gfx.Point(250, 225), "Red")
	example.setOutline("Blue")
	example.draw(win)
	message2 = gfx.Text(gfx.Point(250,290), "You would type 'b' for blue!\n type 'r' for red\n type 'g' for green \n\n\nclick anywhere to start the game!\n GOOD LUCK!")
	message2.draw(win)
	
	#waits for user to click to begin game
	win.getMouse()
	message.undraw()
	example.undraw()
	message2.undraw()	

#plays a countdown from 5 to 0
def play_countdown(): 
	'''plays a countdown from 5 to 0'''
	message = gfx.Text(gfx.Point(250,175), "Get ready!\nGame starts in:")
	message.draw(win)
	time.sleep(1)
	x=5
	while x > -1:
		text = gfx.Text(gfx.Point(250,215), x)
		text.draw(win)
		#delays for 1 second before undrawing 
		time.sleep(1)
		text.undraw()
		x -= 1 
	message.undraw()


#runs the core game 'round' number of times
def play_game(rounds):
	''' input rounds. runs game. returns number correct'''
	cnt = 0
	num_correct = 0
	
	#plays game 'round' number of times
	while cnt < rounds:
		#prints the round number 
		rounds_printer = gfx.Text(gfx.Point(250,200),("Round " + str(cnt + 1) + " of " + str (rounds)))
		rounds_printer.draw(win)
		
		#Creates the word and prints it
		text = gfx.Text(gfx.Point(250,250), "")
		text.setText(get_color())
		color_of_letters = get_color()
		text.setOutline(color_of_letters)
		text.draw(win)
		
		#waits to get the input from the user
		entry = get_color_input()
		
		#evaluates if the entry is correct and adds to the number correct
		if is_answer_correct(entry, color_of_letters):
			num_correct +=1 
			
		#unprints the text to prepare for next round
		text.undraw()
		rounds_printer.undraw()
		
		cnt += 1

	return num_correct
	
	
#determines if the answer is correct 
def is_answer_correct(answer , color):
	'''input an answer and color, returns True if they are the same and false if they are different'''  
	#returns true if first letter of color == answer
	if answer.lower() == color[0].lower():
		return True 
	else:
		return False


#calculates the score of the player
def calculate_score(num_correct , run_length): 
	"""The rating will be the seconds for each correct answer. Basically elapsed time divided by how many correct answer they got. If it is less than 0.8 then they did great, if less than 1 they did Good, and anything else is Poor"""
	# calculates the score
	if num_correct == 0: 
		score = "\n\n You didn't get any correct answers...\n\n -*sigh*- \n\nTry..\nTry..\n Again!"
	else:	
		score = run_length/num_correct
	
	# creates the correct evaluation phrase based on the score
	if num_correct > 0:
		# added this one just for fun
		if score < .4:
			evaluation = "un-FREAKING-believable!" 
		elif score < .8: 
			evaluation = "great!"
		elif score < 1:
			evaluation = "good."
		else: 
			evaluation = "poor.. :("
		
	#creates the string for output of the results
	if num_correct > 0:
		score_str = 'You did ' + evaluation + "\n\nYour score was " + str(round(score, 4)) + ' seconds per correct answer!'
		return score_str
	else:
		return score


#prints the reslults of the game and asks user if they want to play agian
def print_results(score, num_correct, rounds, time):
	"""Input (score string) Output score graphic page, returns playing True or False"""
	
	# creates and prints score graphic 
	results_2 = gfx.Text(gfx.Point(250,190), ("you got " + str(num_correct) + " out of " + str(rounds) + " answers correct!\ngame length: " + str(round(time, 2)) + " seconds!"))
	results_2.draw(win)
	results = gfx.Text(gfx.Point(250,250), score)
	results.draw(win)
	
	# calls play_again function to get whether player wants to keep playing
	play_again_answer = play_again()
	results.undraw()
	results_2.undraw()
	return play_again_answer


def play_again(): 
	""" Creates two buttons for 'Play Again' or 'Exit' Returns True or False""" 
	# runs until user clicks on 'Play Again' or 'Exit'
	while True:
		
		#Draws the play again button
		play_again = gfx.Rectangle(gfx.Point(90 ,350 ), gfx.Point(230 ,425 )) 
		play_again.draw(win)
		play_again_str = gfx.Text(gfx.Point(160,387), "PLAY AGAIN")
		play_again_str.draw(win)
		
		#Draws the quit button
		quit_button = gfx.Rectangle(gfx.Point(270 ,350 ), gfx.Point(410 ,425 )) 
		quit_button.draw(win) 
		quit_str = gfx.Text(gfx.Point(340,387), "EXIT")
		quit_str.draw(win)
		
		#gets a mouse click and evaluates if it falls in the "play again" button or "Exit" button
		answer = win.getMouse()
		
		# sets 'play again' button zone
		# evaluates if click falls in zone
		if (answer.x <= 230 and answer.x >= 90) and (answer.y <=425 and answer.y >= 350):
			play_again.undraw()
			quit_button.undraw()
			play_again_str.undraw()
			quit_str.undraw()
			return True
		
		# sets 'exit' button zone 
		# evaluates if click falls in zone
		elif (answer.x <= 410 and answer.x >= 270) and (answer.y <=425 and answer.y >= 350):
			play_again.undraw()
			quit_button.undraw()
			play_again_str.undraw()
			quit_str.undraw()
			return False
		
		#if click is not on a button clears screen to avoid build up of printed graphic layers	
		play_again.undraw()
		quit_button.undraw()
		play_again_str.undraw()
		quit_str.undraw()
	
	
############################### MAIN PROGRAM RUN ################################################
	
	
# Creates the window for the game
# All functions dependent on this object
win = gfx.GraphWin("Flexible Mind Game!" , 500, 500)

#Creates loop for game
playing = True
while playing: 
	
	# get the number of problems from the user using get_number() set to 'rounds'
	rounds = get_number("Welcome to Flexible Minds!\n\nHow many games would you like to play?\n(Type a number 3 to 20 and press enter)", 3, 20)
	#prints the rules and waits for a click to begin the game
	rules_wait()
	# start count down 
	play_countdown()
	# start timer
	start_time = time.time()
	#runs the game and records the number of correct answers
	num_correct = play_game(rounds)
	#records the end time
	end_time = time.time() 
	#calculates the length of the game
	run_length = end_time - start_time
	#calculate the score
	score = calculate_score(num_correct , run_length)
	#send the score to the results screen
	#results screen returns whether or not the play wants to keep playing
	playing = print_results(score, num_correct, rounds, run_length )
	
win.close() 



