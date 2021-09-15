import time
import pyttsx3
voice = pyttsx3.init()
try:
    arrow = input("Press u for going up and d for going down")
    print("Elevator Door Opens")
    print("W e l c o m e  T o  E l e v a t o r")
    voice.say("Welcome  To  Elevator")
    voice.runAndWait()
    voice.stop()
    print("Elevator Door Closes")
    floor = int(input("Which floor you are at?"))
    go = int(input("Which floor you want to go at?"))
except:
    print("please enter valid number")
finally:
    max = 10
    total = 0
    if arrow == 'u' and go < 11:
        total = go - floor
        if total > 0:
            while floor < go:
                print(floor)
                time.sleep(1)
                floor += 1
            print(f"R e a c h e d  a t  f l o o r  {go}")
            print("Door Opens")
        else: print("Please enter a higher floor number")
    elif arrow == 'd'and go < 11:
        total = floor - go
        if total > 0:
            while floor > go:
                print(floor)
                time.sleep(1)
                floor -= 1
            print(f"R e a c h e d  a t  f l o o r  {go}")
        else: print("Please enter a lower floor number")
    else: print("Not a floor number")
