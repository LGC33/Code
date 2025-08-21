########################################################################
##
## CS 101
## Program # 2
## Name : Larry
## Email : 
##
## PROBLEM : Play blackjack dice against the computer.  You can continue to roll
##              until you bust ( go over 21 ) or decide to hold.  The computer then rolls
##              to try and beat you.  Once the player is out of money the game will be over.
##              The player can buy in with more chips.
##
## ALGORITHM1 : 
##      I1. Display initial welcome
##      I2. Ask for initial money from user.  Assign to chips
##      I3. If chips is less than or equal to zero.  Goto Step I1
##      I4. Set total rounds to zero and highest pot to the number of chips.
##      W1. Get wager amount, assign to wager.
##      W2. if wager less than or equal to zero or wager is greater than chips goto W1
##      W3. increment total rounds.
##      U1. Roll 2 die, add the results and assign to dealer total.  Display the values
##      U2. Roll 2 die for user, add the results and assign to the user total.  Display the values.
##      U3. Ask if the user wants to roll again.  If N, or NO then goto Step D1
##      U4. Roll 1 die again.  Add result to user total and display roll.
##      U5. If User total is less than or equal to 21 Goto Step U3
##      U6. Display that the user busted.
##      U7. Goto L1
##      D1. Roll 1 die and add result to dealer total.  Display the values.
##      D2. if dealer total is greater than 21 goto D7
##      D3. if dealer total is greater than user total goto L1.
##      D5. if dealer total is equal to user total goto TIE1
##      D6. Goto Step D1
##      D7. Display Dealer bust, user wins.  Output rolls.
##      D8. Increment chips by wager amount.
##      D9. If chips greater than highest pot.  Increment highest pot.
##      D10. Goto Step E1
##      TIE1. Display scores and that user tied.
##      TIE2. Goto Step E1.
##      L1. Display User loses.  Show rolls
##      L2. Decrement chips by wager amount.
##      L3. Goto Step E1
##      E1. if chips is greater than 0.  Goto W1
##      E2. Display total total rounds and highest pot.
##      E3. Ask user if they want to play again.
##      E4. If user entered Y, or YES goto Step I1
##      E5. If user entered N, or NO goto step E7
##      E6. Warn user the must enter Y, YES, N or NO. Goto step E3
##      E7. End Program.
##
## ALGORITHM2 :
##      set playing to True
##      while playing
##          set chips to 0
##          while chips <= 0
##              assign chips integer input from user.
##              if chips <= 0 then warn user
##          set rounds played and highest pot to number of chips.
##
##          while chips > 0
##              set wager to 0
##              while wager <= 0 or wager > chips
##                  assign wager the integer input from user.
##                  if wager is invalid warn the user
##
##              Sum the total of 2 dice rolled and assign to dealer total
##              Sum the total of 2 dice rolled and assign to user total
##              while user wants to continue and user total <= 21
##                  Roll single die and add to user total
##                  Display the results
##
##              if user score <= 21
##                  while dealer total is less than users and dealer total <= 21
##                      Roll single die and add to dealer total
##                      Display the results
##
##              if user_score > 21 or dealer_total > user score then
##                  Display the user lost
##                  Decrement chips by wager.
##              elseif user_score > dealer_total or dealer total > 21 then
##                  Display user won
##                  Increment chips by wager.
##              else
##                  Display Tie information.
##
##              Increment Rounds Played
##              if chips > highest_pot then assign highest_pot value of chips
##
##          Display total Rounds and Highest pot.
##          while user input not valid ( Y, YES, N or NO )
##              Get user input.  Warn if invalid
##          If user choose N, or NO then
##              set playing to False
##                  
## 
## ERROR HANDLING:
##      Money in chips must be Greater than 0.
##      Each Wager must be greater than 0 and less than or equal to the chips.
##      When asking to roll again, or play again, the only valid options are Y, N, YES or NO.
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
