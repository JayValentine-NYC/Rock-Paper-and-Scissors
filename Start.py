import random
computerChoices = ["Rock","Paper","Scissors"]
print("Welcome to You RPS Sim")
playerChoice = input('Choose Your Weapon: \n Rock \n Paper \n Scissors \n')

random.shuffle(computerChoices)

cpuPick = computerChoices[0]
print(cpuPick)

if playerChoice == cpuPick :
    print('DRAW, PLAY AGAIN')













