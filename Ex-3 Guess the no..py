#Guess the number
while (True):
     x=int(input("enter the no.\n"))
     if x==25:
        print("you got the no.")
        break
     elif 0<x<12:
        print("this is far lesser than the no. ")
     elif 12<=x<25:
        print("this is lesser but close to the no.")
     elif 25<x<30:
        print("this is greater but close to the no.")
     elif x>=30:
        print("this is far greater than the no.")
        continue
input("Pleae enter to exit")
