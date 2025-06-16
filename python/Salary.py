#Author :Larry Grace    due :Feb 5, 2017
#Assignment: program 2
#
# Algorithm
#1.Display intial welcome banner
#2.Ask the user how many job offers will be they get.
#3.If the job offers is less than or equal to zero. Go back to step 1. Display welcome banner 
#4. Ask the user how many job offers they want to reject.
#5. If the number the user choose to reject is less than or equal to zero or equal to the amount of intial job offers.
#program returns to step 4 and ask the user how many jobs. 
#6.Ask user do they want to see details of all offers press 1 for yes 2 for skip details.
#7.print results in details down to the decimal .
#8.Show which offer is best for you to chose and how much the offer of the salary is.
#9.Show the highest offer you recieved out of all the offers you received. 
#10.Shows you the highest offer before you could choose.
#11. Shows you the difference between the job opportunities you chose and the opportunites you rejected. 
#12. Ask user if they would like to run the simulator again for a different outcome.
#13.If the user entered Y, or Yes go to step 1.
#14.If the user entered N, or NO go to step 16 and quit the program.
#15. Display a banner asking the user that they must enter Y,Yes,N or no. Go to step 12
#16. End program 

import random
running = True
while running:

    print ("Lets start the simulator for salary calcutaions",)

    job_offers = 0    
    while job_offers <= 0:
         job_offers = int(input( "How many recruiters emails have you opened and contacted?==>"))
         if job_offers <= 0:
             print("try a postive number greater than zero")
             print (job_offers)
       
    reject_offers = 0
    while reject_offers <= 0:
        reject_offers = int(input("How many emails do not mention a salary or what the client name?==>"))
        if reject_offers >= job_offers or reject_offers == 0 :
            print ("Has to be postive but less then number of job offers")
            print (reject_offers)


 
    details= 0
    accepted_offer = random.gauss(65,5)
    highest_rejected=0
    max_money = 0
    details= int(input("See details press 1 skip details press 2?==>"))
    while details <1 or details >2:
         details= int(input("Enter 1 or 2 "))
                 
    while details == 1:
              max_money = 0
              cnt =0
              while cnt < reject_offers:
                  
                    offers=random.gauss(65,5)
                    print ("Job #", cnt, " Offer $ ",offers, "rejected")
                    cnt += 1
                    while highest_rejected < offers :
                         highest_rejected= offers
                         max_money=highest_rejected
              if cnt == reject_offers:
                     if max_money<accepted_offer:                        
                        print ("Job title #", cnt, "Salary Offer $ ",accepted_offer, "accepted")
                        cnt +=1
              
              while cnt <=job_offers:
                  
                  offers=random.gauss(65,5)
                  print ("Job title #", cnt, "Salary offerd $ ",offers, "rejected")
                  cnt+=1
                  while max_money < offers:
                     max_money = offers
                  details +=1
    while details == 2:
              max_money = 0
              cnt =0
              while cnt < reject_offers:
                  
                    offers=random.gauss(65,5)
  
                    cnt += 1
                    while highest_rejected < offers :
                         highest_rejected= offers
                         max_money=highest_rejected
              if cnt == reject_offers:
                     if max_money<accepted_offer:                        
                       
                        cnt +=1
              
              while cnt <=job_offers:
                  
                  offers=random.gauss(65,5)
 
                  cnt+=1
                  while max_money < offers:
                     max_money = offers
                  details +=1
    print("Results",)
    print("You chose the offer of",accepted_offer)
    print("The highest offer before you could choose was",highest_rejected)
    print("The highest offer was",max_money)
    print ("You lost out on",max_money-accepted_offer)
    choice = input("Continue ? Y,N")
    if choice.upper() =="Y":
          running = True
    if choice.upper()=="N":
          running = False 


                       
    
      

   

