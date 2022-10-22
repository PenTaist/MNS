# Essentials libraries
import os, time, ping3
from termcolor import colored
from colorama import init, Back

# Colors
red = ['red']
blue = ['blue']
green = ['green']
yellow = ['yellow']
pink = ['pink']
cyan = ['cyan']
magenta = ['magenta']

# Error function
def error():
    os.system('mode con: cols=52 lines=20')
    os.system("color 4")
    os.system("cls")
    print("""
 _______  _______  _______  _______  _______    _ 
(  ____ \(  ____ )(  ____ )(  ___  )(  ____ )  ( )
| (    \/| (    )|| (    )|| (   ) || (    )|  | |
| (__    | (____)|| (____)|| |   | || (____)|  | |
|  __)   |     __)|     __)| |   | ||     __)  | |
| (      | (\ (   | (\ (   | |   | || (\ (     (_)
| (____/\| ) \ \__| ) \ \__| (___) || ) \ \__   _ 
(_______/|/   \__/|/   \__/(_______)|/   \__/  (_)
    """)
    print(" ")
    print("Return to main menu in 5 seconds...")
    time.sleep(5)
    startup()

# Style of console
def startup():
    os.system('mode con: cols=60 lines=20')
    os.system("cls")
    os.system("color a")
    os.system("title [Multi Network Scanner] Created by PenTaist")
    for color in blue:
        print(colored("""
              ▄▄▄▄███▄▄▄▄   ███▄▄▄▄      ▄████████ 
          ▄██▀▀▀███▀▀▀██▄ ███▀▀▀██▄   ███    ███ 
          ███   ███   ███ ███   ███   ███    █▀  
          ███   ███   ███ ███   ███   ███        
          ███   ███   ███ ███   ███ ▀███████████ 
          ███   ███   ███ ███   ███          ███ 
          ███   ███   ███ ███   ███    ▄█    ███ 
          ▀█   ███   █▀   ▀█   █▀   ▄████████▀  
        
        
        """, color), end="")
    for color in magenta:
        print(colored("  [1] 192.168.1.1          [2] 192.168.0.1", color), end="")
    print(" ")
    print(" ")
    print(" ")
    choice = input(Back.BLUE + "Choose an option : ")

    if choice == "1":
        choice1()
    elif choice == "2":
        choice2()
    else:
        error()

# 192.168.1.1
def choice1():
    os.system("cls")
    os.system("color a")

    hosts_up = 0

    ip = "192.168.1."
    
    add = 1

    for color in magenta:
        print(colored("[I] Network Type : 192.168.1.1", color), end="")
        print(" ")
        print(colored("[*] Scanning your network...", color), end="")
        print(" ")
        print(" ")
    
    while add < 255:
        request = ip + str(add)
        reponse = ping3.ping(request)

        if reponse == False:
            hosts_up = hosts_up
        else:
            for color in yellow:
                print(colored("[-] ", color), end="")
                print(colored(request, color), end="")
                print(" ")
            hosts_up = hosts_up + 1

        add = add + 1

    
    print(" ")
    for color in green:
        print(colored(hosts_up, color), end="")
        print(colored(" hosts are online", color), end="")
        print(" ")
        print(" ")

    input(Back.BLUE + "Press any key to return to main menu...")
    
    startup()

# 192.168.0.1
def choice2():
    os.system("cls")
    os.system("color a")

    hosts_up = 0

    ip = "192.168.0."
    
    add = 1

    for color in blue:
        print(colored("[I] Network Type : 192.168.0.1", color), end="")
        print(" ")
    for color in magenta:
        print(colored("[*] Scanning your network...", color), end="")
        print(" ")
        print(" ")
    
    while add < 255:
        request = ip + str(add)
        reponse = ping3.ping(request)

        if reponse == False:
            hosts_up = hosts_up
        else:
            for color in yellow:
                print(colored("[-] ", color), end="")
                print(colored(request, color), end="")
                print(" ")
            hosts_up = hosts_up + 1

        add = add + 1

    
    print(" ")
    for color in green:
        print(colored(hosts_up, color), end="")
        print(colored(" hosts are online", color), end="")
        print(" ")
        print(" ")

    input(Back.BLUE + "Press any key to return to main menu...")
    
    startup()

# Start program
startup()