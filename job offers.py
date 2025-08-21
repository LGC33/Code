#Author :Larry Grace    due :Feb 5, 2017
#Assignment: program 2
#Job offers
# Algorithm
#1.Dispaly intial welcome
#2.Ask user how many job offers will they get.
#3. If job offers is less than or equal to zero. Go to step 1.
#4. Ask the user how many job offers to reject.
#5. If the number you choose to reject is less than or equal to zero or equal to the amount of intial job offers .go to setp 4
#6.Ask user do they want to see details of all offers press 1 for yes 2 for skip details.
#7.print results.
#8.Show which offer you chose and how much it was.
#9.Show which was the highest offer given.
#10.Shows you the highest offer before you could choose.
#11. Shows you how much money you lost out on
#12. Ask do you want try again.
#13.If entered Y, or Yes go to step 1.
#14.If entered N, or NO go to step 16
#15. Warn user thwy must ente Y,Yes,N or no. Go to step 12
#16. End program 

import random
running = True
while running:

    print ("Lets start the simulater",)

    job_offers = 0    
    while job_offers <= 0:
         job_offers = int(input( "How many job offers will you get?==>"))
         if job_offers <= 0:
             print("try a postive number greater than zero")
             print (job_offers)
       
    reject_offers = 0
    while reject_offers <= 0:
        reject_offers = int(input("How many offers should get rejected?==>"))
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
                        print ("Job #", cnt, " Offer $ ",accepted_offer, "accepted")
                        cnt +=1
              
              while cnt <=job_offers:
                  
                  offers=random.gauss(65,5)
                  print ("Job #", cnt, " Offer $ ",offers, "rejected")
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


                       
    
      

   

