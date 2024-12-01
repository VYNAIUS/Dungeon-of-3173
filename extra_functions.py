
from random import random

def chance(num = 0):
    if random() <= num:
        return True
    else:
        return False

def save(V):
    text = "TD_unlocks=["
    for i in V.TD_area_unlocks:
        if i:
            text = text + "1"
        else:
            text = text + "0"
    text = text + "]"
    text = text + '''
TD_high_scores=['''
    for i in V.TD_max_raids:
        text = text + str(i)
    text = text + "]"
    with open(V.file_path, 'w') as file:
        file.write(text)
    print("The game was saved.")