import random
import sys
import argparse


def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-gt', '--gamer_type', default='loser', type=str)
    parser.add_argument ('-ga', '--games_amount', default=10**6, type=int)
    parser.add_argument ('-da', '--doors_amount', default=3, type=int)
 
    return parser

parser = createParser()
namespace = parser.parse_args(sys.argv[1:])

gamer_type = namespace.gamer_type
games_amount = namespace.games_amount
doors_amount = namespace.doors_amount


# Create empty doors pool and place automobile behind the one door
def get_doors(doors_amount):
    doors = {}

    for i in range (doors_amount):
        doors[i] = {
            'automobile' : False,
            'open' : False
        }

    door_automobile = random.randint(0, doors_amount-1)
    doors[door_automobile]['automobile'] = True
    
    return doors


# Open the doors so that 2 remain closed
def open_doors(doors, choise):
        
    doors_open = 0
    for i in doors:
        if doors_open == doors_amount - 2:
            break
        if i == choise:
            continue
        if doors[i]['automobile']:
            continue
        doors[i]['open'] = True
        doors_open += 1

    return doors


# Choise other closed door
def change_choise(doors, choise):

    for i in doors:
        if not doors[i]['open'] and i != choise:
            choise = i
            break

    return choise


# Game
def game():

    wins = 0
    losses = 0

    for _ in range(games_amount):

        doors = get_doors(doors_amount)
        choise = random.randint(0, doors_amount-1)
        doors = open_doors(doors, choise)

        if gamer_type == 'perfect':
            choise = change_choise(doors, choise)

        if doors[choise]['automobile']:
            wins += 1
        else:
            losses += 1

    return wins, losses


wins, losses = game()
wins_percent = round(wins/games_amount*100, 2)
losses_percent = round(losses/games_amount*100, 2)

games_amount = f'{games_amount:,}'.replace(',', ' ')


print(f'----- MONTY HALL GAME ---')
print(f'gamer type: {gamer_type}\ngames amount: {games_amount}\ndoors amount: {doors_amount}')
print(f'wins: {wins_percent}%\nlosses: {losses_percent}%')
print(f'-------------------------')
