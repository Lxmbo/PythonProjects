#Termianl RPG Game
import random, keyboard, time

BossDefeated = 0  
CharHP = 1500
CharStr = 1
EneHp= (random.randint(25,50)+(CharStr * 5))
globalEneAtk = random.randint(1,10)
block = CharHP - random.randint(1,5)
print('You have entered a dungeon! Survive and find your way out!')

def CharAtk():
    damage=random.randint(5,25)+(CharStr*3)
    return damage


def Luck():
        options = ['Wolf', 'Slime','Goblin','Fire Elemental','Bandit','Chest','Book of Strength']
        type = random.choice(options)
        return type


encounter = Luck()
encounter2 =Luck()
encounter3 = Luck()
encounter4 = Luck()
encounter5 = Luck()   
encounter6 = 'BOSS'
encounters=[encounter,encounter2,encounter3,encounter4,encounter5,'Book of Strength, Chest']
moves = 0

while CharHP>=0:
    print('You have come to an fork in the halls please choose a path \n Left(A), Forward(W), Right(D)?')

    def waitForKey():
        key = keyboard.read_key()
        if key in ['a','w','d']:
            return key
        else:
            return None
    
    
    if waitForKey() == 'a':
        print('Left!!')
    elif waitForKey() == 'w':
        print('Forward!!')
    elif waitForKey() == 'd':
        print('Right!')
    else:
        print('Invalid Input')

   
    def Loot():
        global CharStr
        global CharHP
        opt=['Book of Strength','Large Potion of Health']
        spoil=random.choice(opt)
        if spoil == 'Book of Strength':
            print("You've found a Book of Strength and gained power!")
            CharStr = CharStr +1
        else:
            CharHP = CharHP + 25
            print('You found a Large Potion of Healing and gain +25 HP!')


            
    def Choice(encounter):
            if encounter in ['Wolf','Slime','Goblin','Fire Elemental','Bandit']:
                fChoice = int(input("1) Fight \n2) Flee \n"))
                return fChoice
            elif encounter in ['Chest','Book of Strength']:
             oChoice= int(input('1) Open \n2) Ignore \n'))
            return oChoice

    def Fight(encounter):
        global BossDefeated
        global CharHP
        if BossDefeated == 1:
            return
        localEneHp = 0
        if encounter == encounter6:
            localEneHp += 500
        elif encounter in ['Wolf','Slime','Goblin']:
            localEneHp += 100
        else:
            localEneHp += 150

        eMoves = ['Attack','Block']
        
        while localEneHp >= 0:
            
            eneMove = random.choice(eMoves)
            damage = CharAtk()
            if CharHP <= 0:
                print('GAME OVER')
                break
            print(f'Your HP is: {CharHP} \n The {encounter} has {localEneHp} Hit Points!')
            pMove=input('Your Move! \nZ) Attack \nX) Block\n')


            if pMove == 'z' and eneMove == 'Attack':
                localEneHp=localEneHp - damage
                print(f'Your Attack Lands! You did {damage} damage!\n{encounter} has {localEneHp}HP left!')
            elif pMove == 'x':
                print('Blocking!')
            elif pMove == 'z' and eneMove == 'Block':
                print(f'The Enemy Blocked Your Attack and took' +str(damage - 5)+ 'Damage')
                localEneHp = localEneHp - (damage-5)
            else:
                print('Incorrect Input This Could Cost You!')
            if localEneHp <= 0:
                if encounter == encounter6:
                    BossDefeated = 1                    
                print("You've WON! Collect your spoils!!")
                Loot()
                print(f'You have {CharHP}HP left!')
                break

            while CharHP >=0:
                EneAtk= random.randint(5,15)
                if pMove != 'x' and eneMove == 'Attack':
                    print(f'The {encounter} Attacks! and does {EneAtk} Damage!')
                    CharHP = CharHP - EneAtk
                    print(f'You have {CharHP} left!')
                    if CharHP <= 0:
                        break
                    print(f'You Left Yourself Open! The {encounter} Attacks!')
                elif pMove == 'x' and eneMove == 'Attack':
                    print('You Block the Attack and take no Damage')
                else:
                    print('The Enemy Blocked')
                break
        return



    
    while moves < 5 :
        if CharHP <= 0 or BossDefeated == 1:
            break
        print(f'You have run into a {encounters[moves]} what will you do?')
        #if Choice(encounters[moves]) == 2 and encounters[moves] != 'Chest' and encounters[moves] != 'Book of Strength':
            #print('you run')
        
        #elif Choice(encounters[moves]) == 1 and encounters[moves] != 'Chest' and encounters[moves] != 'Book of Strength':
         #   print("Time To FIGHT!!")
          #  Fight(encounters[moves])
        #elif Choice(encounters[moves]) == 1 and encounters[moves] == 'Book Of Strength':
         #   print('You have gained Strength!')
          #  CharStr = CharStr + 1
        #elif Choice(encounters[moves]) == 1 and encounters[moves] == 'Chest':
         #   CharHP = CharHP + 10
          #  print(f'You Open the Chest to find a Potion of Healing, You drink it and feel refreshed!\nYour HP is now {CharHP}')
        if encounters[moves] == 'Book of Strength':
            if Choice(encounters[moves]) == 1:
                print('You have gained Strength!')
                CharStr = CharStr + 1
            else:
                print('You Ignore The Book!')
        elif encounters[moves] == 'Chest':
            if Choice(encounters[moves])==1:
                CharHP = CharHP + 10
                print(f'You Open the Chest to find a Potion of Healing, You drink it and feel refreshed!\nYour HP is now {CharHP}')
            else:
                print('You Ignore the Chest!')
        else:
            if Choice(encounters[moves]) == 1:
                print('Time to FIGHT!!')
                Fight(encounters[moves])
            else:
                print(f'{encounters[moves]} Attacks you as you flee! You took {globalEneAtk} Damage!')
                CharHP = CharHP - globalEneAtk
                if CharHP <= 0:
                    break
                else:continue

        moves = moves + 1
    
        while moves == 5:
            if BossDefeated == 1:
                break
            
            print('!!  BOSS  !!')
            Fight(encounter6)
            if CharHP<=0:
                break
            if BossDefeated == 1:
                time.sleep(3)
                print('You have defeated the Boss...You walk over his corpse and through a door way...into another tunnel')
                time.sleep(3)
                print('...')
                time.sleep(3)
                print('As you walk you see a light...')
                time.sleep(5)
                print('It grows closer...')
                time.sleep(4)
                print('As you pass through the door way..you see a blue sky...and a land with lush green trees..\nTime for your next Adventure.')
                time.sleep(3)
                print('Thanks For Playing!')
                time.sleep(1)
            exit()
            

                
    