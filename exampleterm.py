BROWNEGG = 0.50
WHITEEGG = 0.75
CHOCEGG = 1.50 
RAINBOW = 2.50
eggnumber = float(input("please enter number (1)=brown (2)=white (3)=chocolate (4)=rainbowegg"))

eggamount = float (input("how many eggs"))

discount = 0

if eggnumber == 1: 
    eggtype = BROWNEGG
    if eggamount >= 13 and eggamount <= 97:
        discount = 0.02
    elif eggamount >= 97:
        discount = 0.03
elif eggnumber == 2:
    eggtype = WHITEEGG
    if eggamount >=13 and eggamount <= 97:
        discount = 0.03
    elif eggamount >= 97:
        discount = 0.04
elif eggnumber == 3:
    eggtype = CHOCEGG
    if eggamount >=13 and eggamount <= 97:
        discount = 0.04
    elif eggamount >= 97:
        discount = 0.05
elif eggnumber == 4:
    eggtype = RAINBOW
    if eggamount >=13 and eggamount <= 97:
        discount = 0.05
    elif eggamount >= 97:
        discount = 0.06
    

output = eggamount * eggtype
print(output)

