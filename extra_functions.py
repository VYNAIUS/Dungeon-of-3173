
from random import random

def chance(num = 0):
    if random() <= num:
        return True
    else:
        return False

def meta_save(V):
    with open(V.meta_save_file_path, 'w') as file:
            for key, value in V.__dict__.items():
                if not key in ["consume_discovered", "SM_completed", "TD_area_unlocks", "TD_max_raids", "SM_skip", "RM_areas_cheat", "V_gamma", "bestiary_entries",
                               "enemies_killed", "reaper_enemy_description_unlocks"]:
                    continue
                file.write(f"{key}: {value}\n")
    print("The game was saved.")