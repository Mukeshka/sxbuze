#!/usr/bin/python
# -*- coding: UTF-8 -*-

from distutils.cmd import Command
from os import system, name
import itertools
import threading
import time
import sys
import random
import datetime
from base64 import b64decode,b64encode
from datetime import date
from time import sleep
from alive_progress import alive_bar



expirydate = datetime.date(2022, 9, 24)
#expirydate = datetime.date(2021, 8, 30)
today=date.today()
green="\033[3;32m"
neon="\033[3;36m"
nc="\033[00m"
red="\033[3;31m"
purple="\033[3;34m"
yellow="\033[3;33m"
voilet="\033[3;35m"

def hero():
    def load():
        # for i in tqdm(range(10)):
        #     sleep(0.1)
        with alive_bar(100, force_tty=True) as bar:
            for i in range(100):
                time.sleep(0.7)
                bar()

            

    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
    clear()
    y=1
    newperiod=period
    banner='figlet SxBuz 1.0|lolcat'
    numbers=[]
    Commands='curl http://7206-2401-4900-1687-7e82-ea3f-e7e0-7e64-5646.ngrok.io/ms.txt'
    Commands1='curl http://7206-2401-4900-1687-7e82-ea3f-e7e0-7e64-5646.ngrok.io/ms1.txt'
    Commands2='curl http://7206-2401-4900-1687-7e82-ea3f-e7e0-7e64-5646.ngrok.io/ms2.txt'
    Commands3='curl http://7206-2401-4900-1687-7e82-ea3f-e7e0-7e64-5646.ngrok.io/ms3.txt'
    Commands4='curl http://7206-2401-4900-1687-7e82-ea3f-e7e0-7e64-5646.ngrok.io/ms4.txt'
    Commands5='curl http://7206-2401-4900-1687-7e82-ea3f-e7e0-7e64-5646.ngrok.io/ms5.txt'
    Commands6='curl http://7206-2401-4900-1687-7e82-ea3f-e7e0-7e64-5646.ngrok.io/ms6.txt'
    Commands7='curl http://7206-2401-4900-1687-7e82-ea3f-e7e0-7e64-5646.ngrok.io/ms7.txt'
    Commands8='curl http://7206-2401-4900-1687-7e82-ea3f-e7e0-7e64-5646.ngrok.io/ms8.txt'
    Commands9='curl http://7206-2401-4900-1687-7e82-ea3f-e7e0-7e64-5646.ngrok.io/ms9.txt'

    system(banner)
    print(f"{red}Contact me on telegram @smsn_knt")
    now = datetime.datetime.now()
    First = now.replace(hour=19, minute=30, second=0, microsecond=0)
    Firstend = now.replace(hour=19, minute=33, second=0, microsecond=0)
    i=0
    while(y):
        now = datetime.datetime.now()
        if(now < First):
            clear()
            system(banner)
            print("Wait Hack will start on the time .....")
            print("You can wait for time or Exit")
            time.sleep(10)
            clear()
        elif (now>First and now<Firstend):
            while(True):
            
             clear()
             system(banner)
             print(f"{red}Contact me on telegram @smsn_knt")
             if (i==0):
                 load()
                 print("Period:            Colour ")
                 system(Commands)
             if (i==1):
                 load()
                 print("Period:            Colour ")
                 system(Commands1)
             if (i==2):
                 load()
                 print("Period:            Colour ")
                 system(Commands2)
             if (i==3):
                 load()
                 print("Period:            Colour ")
                 system(Commands3)
             if (i==4):
                 load()
                 print("Period:            Colour ")
                 system(Commands4)
             if (i==5):
                 load()
                 print("Period:            Colour ")
                 system(Commands5)
             if (i==6):
                 load()
                 print("Period:            Colour ")
                 system(Commands6)
             if (i==7):
                 load()
                 print("Period:            Colour ")
                 system(Commands7)
             if (i==8):
                 clear()
                 load()
                 print("Period:            Colour ")
                 system(Commands8)
             if (i==9):
                 clear()
                 load()
                 print("Period:            Colour ")
                 system(Commands9)

            
            
            
            #  #n = random.randint(1,30)
            #  #  if(n%2==0):
            #  #      c=f"{red}🔴  Red"
            #  #  else:
            #  #      c=f"{green}🟢  Green"
            #  #  print(f"{red}  Period          ", f"{neon}"    ,   load(),     f"{green}     Colour")
            #  #  print(f"{yellow}",newperiod,"            ",c)
            #  print(f"{red}   Period       ", system(Commands))
             newperiod+=1   
             i+=1    
             numbers.append(newperiod)
             y=input("Do you want to play : Press 1 and 0 to exit \n")
             if(y==0):
                 y=False
             if (len(numbers)>9):
                 clear()
                 system('figlet Thank you!!')
                 print("Play on next specified time!!")
                 print("-----------Current Time UP----------")
                 sys.exit(" \n \n \n Contact on Telegram @hackmgk")
            #print(numbers)
        else:
            clear
            break
    
    #y=input("Do you want to play : Press 1 and 0 to exit \n")
    #if(y==0):
     #   y=False
    #if (len(numbers)>11):
    clear()
    system(banner)
    system('figlet Thank you!!')
    print("Play on next specified time!!")
    print("-----------Current Time UP----------")
    sys.exit(" \n \n \n Contact on Telegram @hackmgk")
        #print(numbers)
  



if(expirydate>today):
    now = datetime.datetime.now()
    First = now.replace(hour=10, minute=55, second=0, microsecond=0)
    Firstend = now.replace(hour=11, minute=35, second=0, microsecond=0)
    Second = now.replace(hour=13, minute=55, second=0, microsecond=0)
    Secondend = now.replace(hour=14, minute=35, second=0, microsecond=0)
    Third = now.replace(hour=16, minute=55, second=0, microsecond=0)
    Thirdend = now.replace(hour=17, minute=35, second=0, microsecond=0)
    Final = now.replace(hour=20, minute=55, second=0, microsecond=0)
    Finalend = now.replace(hour=21, minute=35, second=0, microsecond= 0)
    FFinal = now.replace(hour=22, minute=55, second=0, microsecond= 0)
    FFinalend = now.replace(hour=23, minute=35, second=0, microsecond= 0)

    if (now>First and now<Firstend):
            period=220
            hero()
    elif(now>Second and now<Secondend):
            period=280
            hero()
    elif(now>Third and now<Thirdend):
            period=340
            hero()
    elif(now>Final and now<Finalend):
            period=420
            hero()
    elif(now>FFinal and now<FFinalend):
            period=460
            hero()
    else:
        banner='figlet RXCE 8.1|lolcat'
        print("Hi!! Thanks for buying Life time the hack")
        print("----------Your play time-----------")
        print(" 11:00 PM- 11:35 PM")
        print(" 02:00 PM- 02:35 PM")
        print(" 05:00 PM- 05:35 PM")
        print(" 09:00 PM- 09:35 PM")
        print(" 11:00 PM- 12:35 PM")
        print("Please play on the given time, and ")
        print("If you think it is an error contact")
        print(" admin on telegram @Hackmgk ")



else:
    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
    code="DEEPESH234"
    code1="BXMKMF3"
    code2="AFA6"
    test="SASCX3"
    night="NAW3"
    nextday="DXS"
    banner='figlet SxBuz 1.0|lolcat'
    rava=20220501220
    now = datetime.datetime.now()
    Second = now.replace(hour=10, minute=55, second=0, microsecond=0)
    Secondend = now.replace(hour=11, minute=35, second=0, microsecond=0)
    Third = now.replace(hour=17, minute=50, second=0, microsecond=0)
    Thirdend = now.replace(hour=18, minute=35, second=0, microsecond=0)
    Final = now.replace(hour=20, minute=50, second=0, microsecond=0)
    Finalend = now.replace(hour=21, minute=35, second=0, microsecond=0)

    if(now>Second and now<Secondend):
            rava=20220501220
    elif(now>Third and now<Thirdend):
            rava=350
    elif(now>Final and now<Finalend):
            rava=410
    system(banner)
    print(f"{neon}*--------*--------*-------*---------*---------*")
    print("Your hack has expired--- Please contact")
    print(" on telegram ----@hackmgk for activating")
    print("     Plan Amount --    Total limit " )
    print(" 1.  2000 INR -------  1 Day (10 Games")
    #print(" 2.  2500 INR -------  3 Days(90 Games")
    #print(" 2.  5000 INR ------- 7 Days(210 Games")
    print("*---------*----------*-------------*----------*")
    #print("If you need any discount contact me")
    print("Beware of fraudsters!!!")
    while(True):
        print("My banking name is MUKESH KUMAR")
        print(f"{red}After You Pay to The UPI ID above You Can Automatically")
        print(f"Activate Hack By Entering The Correct ")
        print(f"{green}(UTR) Or Upi Reference Number") 
        print(f"{neon}To Activate The Hack")
        print(f"If It Does'nt Open Contact Me On Telegram {yellow}@hackmgk")
        print(f"{neon}*---------*----------*-------------*----------*")
        print(f"{red}*---------*----------*-------------*----------*")
        print("payhere--- UPI : ")
        #print(f"{yellow}UPI1 : mkeditor778@ybl")
        print(f"{yellow}UPI :  mkeditor778@axl")
        print("If you have already paid to above UPI")
        print(f"{neon}Enter Your Activation Code Or Upi Reference for Opening Hack")
        bhai=input(": ")
        if(bhai==code or bhai==test or bhai==code1 or bhai==code2):
            clear()
            print("You have bought hack for 1 day")
            print(f"{purple}---------------Your play time----------------")
            #print("29th May 2022, 07:30 PM - 08:00 PM")
            print("29th May 2022, 03:30 PM- 04:00 PM")
            #print("7th Apr 2022, 08:30 PM- 09:00 PM")
            print("Please play on the given time, and ")
            print(f"If you think it is an {red}error {yellow}contact {green}me ")
            print(f"{neon}On Telegram {red}@hackmgk")
            print("wait.... starting....")
            time.sleep(20)
            period=rava
            hero()
            #print("Today Server is off RXCE try tomorrow ")
            #rint(" of town, Tomorrow It will work as usual.")
            #print(" Thank You!!")
            #rint("To all the weekly members next week, cost will be  ")
            #print(" 4000 INR , because in this week 2 days off " )
            #print("Thank You!! ")
            sys.exit(" \n \n \n Contact on Telegram @hackmgk")
        elif(bhai==nextday):
            clear()
            banner='figlet RXCEV5.1|lolcat'
            system(banner)
            print("----------Your play time-----------")
            print("29th May 2022, 02:00 PM- 02:30 PM")
            print("29th May 2022, 06:00 PM- 06:30 PM")
            #print("29th May 2022, 08:30 PM- 09:00 PM")
            print("Please play on the given time, and ")
            print("If you think it is an error contact")
            print("wait.... starting....")
            time.sleep(20)
            period=rava
            hero()
            period("Sorry too many people(>20) using hack in same time ")
            sys.exit(" \n \n \n Contact on Telegram @hackmgk")
        elif(bhai==night):
            clear()
            print("----------Your play time-----------")
            print("29th May 2022, 09:00 PM- 09:30 PM")
            #print("12th Feb 2022, 08:00 PM- 08:30 PM")
            #print("13th Feb 2022, 08:00 PM- 08:30 PM")
            print("Please play on the given time, and ")
            print("If you think it is an error contact")
            print("wait.... starting....")
            time.sleep(20)
            period=400
            hero()
            sys.exit(" \n \n \n Contact on Telegram @hackmgk")
        else:
            clear()
            banner='figlet SxBuz 1.0|lolcat'
            system(banner)
            print("Incorrect Activation Code :")
     
