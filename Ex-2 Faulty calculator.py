#exercise faulty calculator

x=int(input("the first no. is "))
y=int(input("the second no. is"))
print("1 for addition \n2 for multiplication\n3 for subtraction\n4 for division")
choice=int(input("operation is "))


if x==45 and y==3 and choice==1:
    print("answer",int(555))
elif x==56 and y==9 and choice==2:
    print("answer", int(54))
elif x==56 and y==6 and choice==4:
    print("answer", int(4))
elif choice==1:
    print("answer of addition",x+y)
elif choice==2:
    print("answer of multiplication", x*y)
elif choice==3:
    print("answer of sutraction", x-y)
elif choice ==4:
    print("answer of division is", x/y)
input("")
