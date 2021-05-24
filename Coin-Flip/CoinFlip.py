#This code flips a coin however many times the user decides. 
#It will also record the outcomes and count the number of tails and heads.

import random

def coin_flip(times):
    heads=0
    tails=0
    for times in range(times):
        choice=random.choice(["heads","tails"])
        
        if choice=="heads":
            heads+=1
            print("heads")
            
        else:
            tails+=1
            print("tails")
            
    print("heads count: " + str(heads))
    print("tails count: " + str(tails))
