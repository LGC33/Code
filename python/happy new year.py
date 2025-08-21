#Wish Happy New Year 2023
import pyfiglet 
import time 
from termcolor import colored,cprint 
wish =['Happy','New','Year','2023']
count=0
colors=['green','yellow','magenta','cyan']
for i in range(1,1000):
    if(count>3):
        count=0
        cprint('*'*60,'red')
    else:
        color=colors[count]
        msg = pyfiglet.figlet_format(wish[count],
        font='starwars',
        width = 150)
        cprint(msg,color)
        count = count + 1
        time.sleep(0.7)