import time
print("Elevator Door Opens")
print("W e l c o m e  T o  E l e v a t o r")
print("Elevator Door Closes")
floor = int(input("Which floor you are at?"))
go = int(input("Which floor you want to go at?"))
max = 10
total = 0
if go and floor in range(0,11) :
    total = go - floor
    if total > 0:
        while floor < go:
            print(floor)
            time.sleep(1)
            floor += 1
        print(f"R e a c h e d  a t  f l o o r  {go}")
        print("Door Opens")
    elif total < 0:
        while floor > go:
            print(floor)
            time.sleep(1)
            floor -= 1
        print(f"R e a c h e d  a t  f l o o r  {go}")
else:
    print("Not a floor number")
