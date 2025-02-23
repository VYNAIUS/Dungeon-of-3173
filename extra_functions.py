
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
                               "enemies_killed", "reaper_enemy_description_unlocks", "encyclopedia_consumable_items_entries", "encyclopedia_recipe_entries"]:
                    continue
                file.write(f"{key}: {value}\n")
    print("The game was saved.")

def meta_options(V):
    while True:
        print('''1. Gameplay
2. Visuals
9. Back
Type in the number or the action itself...''')
        action = input()
        if action.lower() in ["1", "gameplay"]:
            while True:
                print("1. Skip Story Mode requirements -", V.SM_skip)
                if V.SM_completed or V.SM_skip:
                    print("2. Unlock all Raid Mode areas -", V.RM_areas_cheat)
                else:
                    print("2. Locked")
                print("9. Back")
                print("Type in the number or the action itself...")
                action = input()
                if action.lower() in ["1", "skip story mode requirements"] or "skip" in action.lower() or "story mode" in action.lower():
                    if V.SM_skip:
                        V.SM_skip = False
                        if V.SM_completed == False:
                            V.RM_areas_cheat = False
                    else:
                        V.SM_skip = True
                elif (action.lower() in ["2", "unlock all raid mode areas"] or "raid" in action.lower()) and (V.SM_completed or V.SM_skip):
                    if V.RM_areas_cheat:
                        V.RM_areas_cheat = False
                    else:
                        V.RM_areas_cheat = True
                elif action.lower() in ["9", "back"]:
                    break
        elif action.lower() in ["2", "visuals"]:
            while True:
                print("1. Map Gamma/Brightness -", V.V_gamma)
                print("2. Graphics Quality - Low")
                print("9. Back")
                print("Type in the number or the action itself...")
                action = input()
                if action.lower() in ["1", "map", "gamma", "brightness"] or "gamma" in action.lower() or "bright" in action.lower():
                    print("Please insert a float value between 0 and 2. Leave blank if you want to reset it.")
                    action = input()
                    try:
                        action = float(action)
                        V.V_gamma = action
                    except:
                        V.V_gamma = 1
                elif action.lower() in ["2", "graphics", "quality"] or "graphics" in action.lower() or "quality" in action.lower():
                    print('''An error has occured: your device cannot render higher quality graphics!
Type anything to continue...''')
                    action = input()
                    break
                elif action.lower() in ["9", "back"]:
                    break
        elif action == "9" or "back" in action.lower():
            break
    meta_save(V)