from pynput.keyboard import Key,Controller
import time
from datetime import datetime
import threading






keyboard = Controller()




print("      .o.                     .    o8o                            .                   .o8 \n"
      "     .888.                  .o8    ` '                          .o8                   888 \n"
      "    .8 888.      .ooooo.  .o888oo oooo  oooo    ooo  .oooo.   .o888oo  .ooooo.   .oooo888 \n"
      "   .8' `888.    d88' ` Y8   888   `888   `88.  .8'  `P  )88b    888   d88' `88b d88' `888 \n"
      "  .88ooo8888.   888         888    888    `88..8'    .oP 888    888   888ooo888 888   888 \n"
      " .8'     `888.  888   .o8   888 .  888     `888'    d8(  888    888 . 888    .o 888   888 \n"
      "o88o     o8888o `Y8bod8P'   888  o888o     `8'     `Y888""8o   888  `Y8bod8P' `Y8bod88P")

time_now = 5
timer = 0
while time_now != timer:
    time.sleep(1)
    timer += 1
    if timer == time_now:
        break
    if timer == 1:
        print("starting in 5-seconds")
    if timer == 2:
        print("starting in 4-seconds")
    if timer == 3:
        print("3-seconds")
    if timer == 4:
        print("2-seconds")
    if timer == 5:
        print("Starting....")

def say(word):
    timer = 100000000
    time_now = 1
    amount = 10000000
    current = 1
    while current != amount:
        time.sleep(1)
        current += 1
        print(" _______  _______  __    _  _______ \n" 
              "|       ||       ||  |  | ||       | \n"
              "|  _____||    ___||   |_| ||_     _| \n"
              "| |_____ |   |___ |       |  |   | \n"
              "|_____  ||    ___||  _    |  |   | \n"
              " _____| ||   |___ | | |   |  |   | \n"  
              "|_______||_______||_|  |__|  |___| \n")
        print(current)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        keyboard.type(word + current_time)
        keyboard.press(Key.enter)


thread1 = threading.Thread(target=say(" Rawr "))





thread1.start()



