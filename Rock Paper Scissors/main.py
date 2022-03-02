import random

def game(comp,you):
    if comp == you:
        return None

    elif comp == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True

    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True

    elif comp == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True                              

comp = random.randint(1, 3)
if comp == 1:
    comp = 'r'
elif comp == 2:
    comp = 'p'
elif comp == 3:
    comp == 's'       

 

you=input("Enter: Rock(r) Paper(p) Scissors(s): ")

a = game(comp, you)

if a == None:
    print("---------------------Match Draw------------------")
elif a:
    print("-----------------------You Win-------------------")    
else:
    print("-----------------------You Lose------------------")    

