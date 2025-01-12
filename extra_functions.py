
from random import random

def chance(num = 0):
    if random() <= num:
        return True
    else:
        return False

def meta_save(V):
    with open(V.meta_save_file_path, 'w') as file:
            for key, value in V.__dict__.items():
                if not key in ["SM_completed", "TD_area_unlocks", "TD_max_raids", "SM_skip", "RM_areas_cheat"]:
                    continue
                file.write(f"{key}: {value}\n")
    print("The game was saved.")