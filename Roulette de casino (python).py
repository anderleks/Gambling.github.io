from random import *

X=input("Rouge ou Noir ? -> ")
if X!="Rouge":
    if X=="Noir":
        U=randint(1,2)
        if X=="Rouge":
            Y=1
        else:
            Y=2
        if Y==U:
            print("C'est gagné !!! ")
        else:
            print("C'est perdu")
    else:
        print("Choisissez entre le Rouge ou le Noir ") 
else:
    U=randint(1,2)
    if X=="Rouge":
        Y=1
    else:
        Y=2
    if Y==U:
        print("C'est gagné !!! ")
    else:
        print("C'est perdu")
        
    